//本章开始的是算法和数据操作
/*
    此时我刚刚在bilibili上看过一段关于poping的视频，内心难掩身体震爆的节奏;
    看着Atom上震动的屏幕特效，我不禁问我自己，为什么我不能把心情跟代码一同写进这个该死的库里;
    于是我就写下了这样的一段话；
    哦，现在耳机里放的是这首曲子，你们可以搜一下@_@，去网易云搜就好啦，写代码贼带感。。
    好吧，继续我们今天的剑指offer了。
*/


//递归和循环

//刚刚身后飘过一个美女，这让我的目光不由地跟着她动了一下，我眼看着她消失在了不远的楼道拐弯处；
//就在我这段话还没有写完的同时，她又从我后面飘过去了，这次我没有看她；因为我已经沉浸在了写字的喜悦里；
//我忽然发现我写字的时候，内心是如此的活蹦乱跳，我觉得这是一个信号！

//所以我要写代码了
int addFromToN_Recursive(int n)
{
    return n <= 0? 0 : n + addFromToN_Recursive(n - 1);
}
//上面这个代码写的真是鬼斧神工，
//老子以前都是用if else写的，为什么我就想不到用条件表达式
//我想写下上面这段的人一定是个处女座

int addFromToN_Iterative(int n)
{
    int result = 0;
    for (size_t i = 0; i <= n; i++) {
        result += i;
    }
    return result;
}

//果然还是递归比较优雅而且（令众码民）沁人心脾；
//我喜欢这样简洁而毫无保留的表达，（what？什么叫毫无保留的表达？

//接下来要进入正题了
//斐波那契数列
long long fibonacci(unsigned int n)
{
    if (n <= 0) {
        return 0;
    }

    if (n == 1) {
        return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

//我们换一种解法
long long fibonacci(unsigned n)
{
    int result[2] = {0, 1};
    if (n < 2)
        return result[n];

    long long fibNMinusOne = 1;
    long long fibNMinusTwo = 0;
    long long fibN = 0;

    for (size_t i = 2; i <= n; i++){
        fibN = fibNMinusOne + fibNMinusTwo;

        fibNMinusTwo = fibNMinusOne;
        fibNMinusOne = fibN;
    }

    return fibN;
}
