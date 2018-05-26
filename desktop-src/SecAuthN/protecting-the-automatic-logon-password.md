---
Description: The automatic logon password should be protected by using the LsaStorePrivateData function.
ms.assetid: 7bd4d725-de17-4801-bd06-8d47a777409d
title: Protecting the Automatic Logon Password
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Protecting the Automatic Logon Password

The automatic logon password should be protected by using the [**LsaStorePrivateData**](security.lsastoreprivatedata) function.

The following example shows how to protect the automatic logon password. The example retrieves a handle to the [**Policy**](security.policy_object) object by calling the [**LsaOpenPolicy**](/windows/win32/Ntsecapi/nf-ntsecapi-lsaopenpolicy?branch=master) function. For more information about the **Policy** object and **Policy** object handles, see **Policy** object and [Opening a Policy Object Handle](security.opening_a_policy_object_handle), respectively. The example then sets the protected password by calling the [**LsaStorePrivateData**](security.lsastoreprivatedata) function. Note that if the caller passes in **NULL** for the protected password value, then the code clears the existing protected password. Before exiting, the code closes the handle to the **Policy** object.


```C++
#include <windows.h>
#include <stdio.h>

DWORD UpdateDefaultPassword(WCHAR * pwszSecret)
{

    LSA_OBJECT_ATTRIBUTES ObjectAttributes;
    LSA_HANDLE LsaPolicyHandle = NULL;

    LSA_UNICODE_STRING lusSecretName;
    LSA_UNICODE_STRING lusSecretData;
    USHORT SecretNameLength;
    USHORT SecretDataLength;

    NTSTATUS ntsResult = STATUS_SUCCESS;
    DWORD dwRetCode = ERROR_SUCCESS;

    //  Object attributes are reserved, so initialize to zeros.
    ZeroMemory(&amp;ObjectAttributes, sizeof(ObjectAttributes));

    //  Get a handle to the Policy object.
    ntsResult = LsaOpenPolicy(
        NULL,    // local machine
        &amp;ObjectAttributes, 
        POLICY_CREATE_SECRET,
        &amp;LsaPolicyHandle);

    if( STATUS_SUCCESS != ntsResult )
    {
        //  An error occurred. Display it as a win32 error code.
        dwRetCode = LsaNtStatusToWinError(ntsResult);
        wprintf(L"Failed call to LsaOpenPolicy %lu\n", dwRetCode);
        return dwRetCode;
    } 

    //  Initialize an LSA_UNICODE_STRING for the name of the
    //  private data ("DefaultPassword").
    SecretNameLength = (USHORT)wcslen(L"DefaultPassword");
    lusSecretName.Buffer = L"DefaultPassword";
    lusSecretName.Length = SecretNameLength * sizeof(WCHAR);
    lusSecretName.MaximumLength =
        (SecretNameLength+1) * sizeof(WCHAR);

    //  If the pwszSecret parameter is NULL, then clear the secret.
    if( NULL == pwszSecret )
    {
        wprintf(L"Clearing the secret...\n");
        ntsResult = LsaStorePrivateData(
            LsaPolicyHandle,
            &amp;lusSecretName,
            NULL);
        dwRetCode = LsaNtStatusToWinError(ntsResult);
    }
    else
    {
        wprintf(L"Setting the secret...\n");
        //  Initialize an LSA_UNICODE_STRING for the value
        //  of the private data. 
        SecretDataLength = (USHORT)wcslen(pwszSecret);
        lusSecretData.Buffer = pwszSecret;
        lusSecretData.Length = SecretDataLength * sizeof(WCHAR);
        lusSecretData.MaximumLength =
            (SecretDataLength+1) * sizeof(WCHAR);
        ntsResult = LsaStorePrivateData(
            LsaPolicyHandle,
            &amp;lusSecretName,
            &amp;lusSecretData);
        dwRetCode = LsaNtStatusToWinError(ntsResult);
    }

    LsaClose(LsaPolicyHandle);

    if (dwRetCode != ERROR_SUCCESS)
        wprintf(L"Failed call to LsaStorePrivateData %lu\n",
            dwRetCode);
    
    return dwRetCode;

}

```



Note that if Winlogon cannot find a password stored by the [**LsaStorePrivateData**](security.lsastoreprivatedata) function, it will use the **DefaultPassword** value of the Winlogon key (if it exists) for the automatic logon password.

For more information about automatic logon and the Winlogon registry key, see [MSGina.dll Features](msgina-dll-features.md).

For more information about protecting passwords, see [Handling Passwords](security.handling_passwords).

 

 



