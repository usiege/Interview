/*!
* 图的矩阵主要包含四个数据：
*
* - `matrix`：图的矩阵表示，类型为`MatrixGraph<N>`
* - `adjList`：图的邻接表表示，类型为`ADJListGraph<N>`
* - `vertexes`：顶点集合，类型为`std::array<std::shared_ptr<VertexType>,N>`。它是一个`std::array`，其元素类型为指向顶点的强引用
* - `next_empty_vertex`：顶点集合中，下一个为空的位置，类型为`std::size_t`。它用于添加顶点。

* 图支持插入、修改顶点操作，插入、修改边操作（由图的矩阵以及图的邻接表来代理），以及返回边、返回权重（由图的矩阵以及图的邻接表来代理）。
*
*/
#ifndef GRAPH
#define GRAPH

#include <array>
#include <memory>
#include <assert.h>

template<unsigned N, typename VType> struct Graph
{
    typedef int VIDType; //顶点编号类型
    typedef int EWeightType; //权重类型

    typedef std::tuple<VIDType, VIDType, EWeightType> EdgeTupleType; //边
    typedef VType VertexType; //顶点
    static const unsigned NUM = N;

    //!显式构造函数，为图的矩阵指定`invalid_weight`
    /*!
    * \param  val:无效权重值
    */
    explicit Graph(EWeightType val):matrix(val), next_empty_vertex(0){}
    //!默认构造函数
    Graph:next_empty_vertex(0){}

    std::array<std::shared_ptr<VertexType>,N> vertexes;
    std::size_t next_empty_vertex;

    //这里的邻接矩阵和邻接表尚未定义
    MatrixGraph<N> matrix;      //图的邻接矩阵
    ADJListGraph<N> adjList;    //图的邻接表


    //!add_vertex:添加一个顶点
    /*!
    * \param  key:顶点存放的数据
    * \return: 顶点的id
    *
    * 如果已经有了N个顶点，则图的顶点已满，则抛出`std::invalid_argument`异常.
    *
    * 在每一次添加顶点之前会从`next_empty_vertex·指定的位置处开始寻找可以添加顶点的地方。如果找不到可以添加顶点的地方，则抛出`std::invalid_argument`异常
    */
    VIDType add_vertex(const typename VertexType::KeyType& key)
    {
        while (next_empty_vertex < N && vertexes.at(next_empty_vertex)) {
            next_empty_vertex++;
        }
        if (next_empty_vertex >= N) {
            throw std::invalid_argument("图结点已满");
        }

        VIDType v_id = next_empty_vertex;
        vertexes.at(next_empty_vertex) = std::make_shared<VertexType>(key, v_id);
        next_empty_vertex++;
        return v_id;
    }
    //!add_vertex:添加一个顶点
    /*!
    * \param  key:顶点存放的数据
    * \param id:指定该顶点的`id`
    * \return: 顶点的id
    *
    * - 如果`id<0`或者`id>=N`，则抛出异常。因为正常的顶点`id`在`[0,N)`之间
    * - 如果已经存在某个顶点的`id`为指定的`id`，则抛出异常
    */
    VIDType add_vertex(const typename VertexType::KeyType& key, VIDType id)
    {
        if (id < 0 || id >= N) {
            throw std::invalid_argument("id must >=0 and <N");
        }
        if (vertexes.at(id)) {
            throw std::invalid_argument("id has existed.");
        }
        vertexes.at(id) = std::make_shared<VertexType>(key, id);
        return id;
    }
    //!modify_vertex:修改一个顶点的数据
    /*!
    * \param  newkey:新的数据
    * \param id:指定该顶点的`id`
    *
    * - 如果`id<0`或者`id>=N`，则抛出异常。因为正常的顶点`id`在`[0,N)`之间
    * - 如果不存在某个顶点的`id`为指定的`id`，则抛出异常
    */
    void modify_vertex(const typename VertexType::KeyType &newkey, VIDType id)
    {
        if (id < 0 || id >= N) {
            throw std::invalid_argument("must >= 0 and < N");
        }
        if (!vertexes.at(id)) {
            throw std::invalid_argument("id does not exist.");
        }
        vertexes.at(id)->key = newkey;
    }

/* 乱入的广告
    🔥66狂欢季-Robert Oatley优惠活动
     
    3、Robert Oatley超级疯抢日
    活动时间：北京时间6月11日10:00-24:00
*/
    //!add_edge:添加一条边
    /*!
    * \param  edge_tuple:一条边的三元素元组
    *
    * 为了便于计算，添加边时并不是添加`Edge`类型，而是`std::tuple<VIDType,VIDType,EWeightType>`类型的值。
    *
    * 添加边之前如果边指定的任何一个顶点无效，则抛出异常：
    *
    * - 如果指定的顶点`id`不在`[0,N)`之间，则无效
    * - 如果不存在某个顶点与指定的顶点`id`相同，则无效
    *
    * 在添加边时，同时向图的矩阵、图的邻接表中添加边
    *
    * 如果添加的边是无效权重，则直接返回而不添加
*/
    void add_edge(const EdgeTupleType& edge_tuple)
    {
        auto id1 = std::get<0>(edge_tuple);
        auto id2 = std::get<1>(edge_tuple);

        if (id1 < 0 || id1 >= N || id2 < 0 || id2 >= N) {
            throw std::invalid_argument("add edge error:id must >=0 and < N");
        }
        if (!vertexes.at(id1) || !vertexes.at(id2)) {
            throw std::invalid_argument("add edge error: vertex of id does not exist.");
        }
        if (std::get<2>(edge_tuple) == matrix.invalid_weight) {
            return;
        }

        matrix.add_edge(edge_tuple);
        adjList.add_edge(edge_tuple);
    }

    //!add_edges:添加一组边
    /*!
    * \param  begin:边容器的起始迭代器
    * \param  end:边容器的终止迭代器
    *
    * 为了便于计算，添加边时并不是添加`Edge`类型，而是`std::tuple<VIDType,VIDType,EWeightType>`类型的值
    *
    * 在添加边时，同时向图的矩阵、图的邻接表中添加边
    */
    template<typename Iterator> void add_edges(const Iterator&begin ,const Iterator&end)
    {

        if(std::distance(begin,end)<=0)
            return;
        Iterator iter=begin;
        while(iter!=end)
        {
            add_edge(*iter);
            iter++;
        }
    }

    //!adjust_edge:修改一条边的权重
    /*!
    * \param  id1:待修改边的第一个顶点
    * \param  id2:待修改边的第二个顶点
    * \param  wt:新的权重
    *
    * 修改边权重之前如果边指定的任何一个顶点无效，则抛出异常：
    *
    * - 如果指定的顶点`id`不在`[0,N)`之间，则无效
    * - 如果不存在某个顶点与指定的顶点`id`相同，则无效
    */
    void adjust_edge(VIDType id1,VIDType id2,EWeightType wt)
    {
        if(id1<0||id1>=N||id2<0||id2>=N)
            throw std::invalid_argument("adjust edge error:id must >=0 and <N.");
        if(!vertexes.at(id1) || !vertexes.at(id2))
            throw std::invalid_argument("adjust edge error: vertex of id does not exist.");
        matrix.adjust_edge(id1,id2,wt);
        adjList.adjust_edge(id1,id2,wt);
    }


    //!has_edge:返回图中指定顶点之间是否存在边
    /*!
    * \param id_from: 第一个顶点的`id`
    * \param id_to: 第二个顶点的`id`
    * \return  :第一个顶点和第二个顶点之间是否存在边
    *
    * 要求图的矩阵和图的邻接表都返回同样的结果
    *
    *  如果边指定的任何一个顶点无效，则抛出异常：
    *
    * - 如果指定的顶点`id`不在`[0,N)`之间，则无效
    * - 如果不存在某个顶点与指定的顶点`id`相同，则无效
    */
    bool has_edge(VIDType id_from,VIDType id_to) const
    {
        if(id_from<0||id_from>=N||id_to<0||id_to>=N)
            throw std::invalid_argument("has edge error:id must >=0 and <N.");
        if(!vertexes.at(id_from) || !vertexes.at(id_to))
            throw std::invalid_argument("has edge error: vertex of id does not exist.");
       auto m=matrix.has_edge(id_from,id_to);
       auto a=adjList.has_edge(id_from,id_to);
       assert(matrix.has_edge(id_from,id_to)==adjList.has_edge(id_from,id_to));
       return matrix.has_edge(id_from,id_to);
    }

    //!weight:返回图中指定顶点之间的边的权重
    /*!
    * \param id_from: 第一个顶点的`id`
    * \param id_to: 第二个顶点的`id`
    * \return  :第一个顶点和第二个顶点之间的边的权重
    *
    * 要求图的矩阵和图的邻接表都返回同样的结果
    *
    *  如果边指定的任何一个顶点无效，则抛出异常：
    *
    * - 如果指定的顶点`id`不在`[0,N)`之间，则无效
    * - 如果不存在某个顶点与指定的顶点`id`相同，则无效
    */
    EWeightType weight(VIDType id_from,VIDType id_to) const
    {
        if(id_from<0||id_from>=N||id_to<0||id_to>=N)
            throw std::invalid_argument("edge weight error:id must >=0 and <N.");
        if(!vertexes.at(id_from) || !vertexes.at(id_to))
            throw std::invalid_argument("edge weight error: vertex of id does not exist.");
        assert(matrix.weight(id_from,id_to)==adjList.weight(id_from,id_to));
        return matrix.weight(id_from,id_to);
    }

};

#endif
