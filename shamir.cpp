#include <bits/stdc++.h>
using namespace std;

int main()
{
	long long int a=1234,k,n,x[1000],v[1000],s;
	srand (time(NULL));
	cin>>k;
	cin>>n;
	for(int i=1;i<k;i++)
	{
		x[i]=rand();
		cout<<x[i]<<endl;
	}
//	x[1]=166;
//	x[2]=94;
	for(int i=1;i<=n;i++)
	{
		s=a;
		for(int j=1;j<k;j++)
		{
			s=s+(x[j]*pow(i,j));
		}
		v[i]=s;
	}

	for(int i=1;i<=n;i++)
	{
		cout<<i<<"="<<v[i]<<endl;
	}

	int b[10000];
	for(int i=0;i<k;i++)
	{
		cout<<i<<" enter: ";
		cin>>b[i];
	}

	

}