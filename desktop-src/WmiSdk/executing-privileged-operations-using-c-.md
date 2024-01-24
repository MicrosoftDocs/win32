---
description: Special client applications might invoke privileged operations.
ms.assetid: e09fcadc-282f-4f07-b69c-b15bfdb07a7d
ms.tgt_platform: multiple
title: Executing Privileged Operations Using C++
ms.topic: article
ms.date: 05/31/2018
---

# Executing Privileged Operations Using C++

Special client applications might invoke privileged operations. For example, an application could allow a manager to reboot an unresponsive office computer. By using Windows Management Instrumentation (WMI), you can execute a privileged operation by calling the WMI provider for the privileged operation.

The following procedure describes how to call a provider for a privileged operation.

**To call a provider for a privileged operation**

1.  Obtain permissions for the client process to execute the privileged operation.

    Typically, an administrator sets the permissions using system administrative tools—prior to running the process.

2.  Obtain permission for the provider process to enable the privileged operation.

    Typically, you can set provider permissions with a call to the [**AdjustTokenPrivileges**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges) function.

3.  Obtain permission for the client process to enable the privileged operation.

    This step is necessary only if the provider is local to the client. If the client and provider exist on the same computer, the client must specifically enable the privileged operation by using one of the following techniques:

    -   If the client owns the process, the client can use [**AdjustTokenPrivileges**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges) to adjust the process token before calling WMI. In this case, you do not need to code any further.
    -   If the client cannot access the client token, the client can use the following procedure to create a thread token and use [**AdjustTokenPrivileges**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges) on that token.

The following procedure describes how to create a thread token and use [**AdjustTokenPrivileges**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges) on that token.

**To create a thread token and use AdjustTokenPrivileges on that token**

1.  Create a copy of the process token by calling [**ImpersonateSelf**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-impersonateself).
2.  Retrieve the newly created thread token by calling [**GetTokenInformation**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-gettokeninformation).
3.  Enable the privileged operation with a call to [**AdjustTokenPrivileges**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges) on the new token.
4.  Obtain a pointer to [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices).
5.  Cloak the pointer to [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) with a call to [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket).
6.  Repeat steps 1 through 5 on each call to WMI.

    > [!Note]  
    > You must repeat the steps because COM caches tokens incorrectly.

     

The code example in this topic requires the following \#include statement to correctly compile.


```C++
#include <wbemidl.h>
```



The following code example shows how to enable privileges on a local machine.


```C++
// Get the privileges 
// The token has been obtained outside the scope of this code sample
// ================== 
DWORD dwLen;
bool bRes;
HANDLE hToken;

// obtain dwLen
bRes = GetTokenInformation(
  hToken, 
  TokenPrivileges, 
  NULL, 
  0,
  &dwLen
); 

BYTE* pBuffer = new BYTE[dwLen];
if(pBuffer == NULL)
{
  CloseHandle(hToken);
  return WBEM_E_OUT_OF_MEMORY;
} 

bRes = GetTokenInformation(
  hToken, 
  TokenPrivileges, 
  pBuffer,     
  dwLen,        
  &dwLen
);

if (!bRes)
{
  CloseHandle(hToken);
  delete [] pBuffer;
  return WBEM_E_ACCESS_DENIED;
} 

// Iterate through all the privileges and enable them all
// ====================================================== 
TOKEN_PRIVILEGES* pPrivs = (TOKEN_PRIVILEGES*)pBuffer;
for (DWORD i = 0; i < pPrivs->PrivilegeCount; i++)
{
  pPrivs->Privileges[i].Attributes |= SE_PRIVILEGE_ENABLED;
} 
// Store the information back in the token
// ========================================= 
bRes = AdjustTokenPrivileges(
  hToken, 
  FALSE, 
  pPrivs, 
  0, NULL, NULL
);

delete [] pBuffer;
CloseHandle(hToken); 

if (!bRes)
  return WBEM_E_ACCESS_DENIED;
else
  return WBEM_S_NO_ERROR;
```



 

 
