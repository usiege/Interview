//1
class CMyString{
public:
	CMyString(char* pData = nullptr);
	CMyString(const CMyString& str);
	~CMyString(void);

private:
	char* m_pData;
}

CMyString& CMyString::operator =(const CMyString &str)
{
	if(this == &str)
		return *this;

	delete []m_pData;
	m_pData = nullptr;

	m_pData = new char[strlen(str.m_pData) + 1];
	strcpy(m_pData, str.m_pData);

	return *this;
}

CMyString& CMyString::operator =(const CMyString &str)
{
	if(this != &str)
	{
		CMyString strTemp(str);

		char* pTemp = strTemp.m_pData;
		strTemp.m_pData = m_pData;
		m_pData = pTemp;
	}
	return *this;
}

//2 单例加同步锁伪代码 C#
public class Singleton()
{
	private Singleton()

	private static object syncObj = new object();
	private static Singleton instance = null;

	public static Singleton instance
	{
		get{
			if (instance == null) // important I
			{
				lock(syncObj){ // important II
					if (instance == null) // important III
					{
						instance = new Singleton();
					}
				}
			}
			return instance;
		}
	}
}
