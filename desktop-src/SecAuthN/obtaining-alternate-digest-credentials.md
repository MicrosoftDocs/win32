---
Description: To obtain credentials other than those associated with the current logon session, populate a SEC\_WINNT\_AUTH\_IDENTITY structure with information for the alternate security principal.
ms.assetid: f590ddb5-39a1-4d0c-a787-da938a63c206
title: Obtaining Alternate Digest Credentials
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Alternate Digest Credentials

To obtain [*credentials*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) other than those associated with the current logon [*session*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50), populate a [**SEC\_WINNT\_AUTH\_IDENTITY**](/windows/desktop/api/Rpcdce/ns-sspi-_sec_winnt_auth_identity_a) structure with information for the alternate [*security principal*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50). Pass the structure to the [**AcquireCredentialsHandle**](/windows/desktop/api/Sspi/) function using the *pAuthData* parameter.

The following table describes the members of the [**SEC\_WINNT\_AUTH\_IDENTITY**](/windows/desktop/api/Rpcdce/ns-sspi-_sec_winnt_auth_identity_a) structure.



| Member             | Description                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **User**           | Null-terminated string containing the name of the security principal whose credentials will be used to establish a security context. |
| **UserLength**     | The length of the **User** member, in characters. Omit the terminating null.                                                         |
| **Domain**         | Null-terminated string that identifies the domain containing the account of the security principal.                                  |
| **DomainLength**   | The length of the **Domain** member, in characters. Omit the terminating null.                                                       |
| **Password**       | Null-terminated string containing the password of the security principal.                                                            |
| **PasswordLength** | The length of the **Password** member, in characters. Omit the terminating null.                                                     |
| **Flags**          | Indicates whether the string members are in ANSI or [*Unicode*](https://msdn.microsoft.com/264f6cb6-36c6-4cdb-b7bb-a5dbd332adcb) format.  |



 

The following table lists the valid values for the **Flags** member of the structure.



| Constant                            | Description                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------|
| SEC\_WINNT\_AUTH\_IDENTITY\_ANSI    | Strings in this structure are in ANSI format.                                                                    |
| SEC\_WINNT\_AUTH\_IDENTITY\_UNICODE | Strings in this structure are in [*Unicode*](https://msdn.microsoft.com/264f6cb6-36c6-4cdb-b7bb-a5dbd332adcb) format. |



 

The structure and constants are declared in the Rpcdce.h header file distributed with the Platform Software Development Kit (SDK).

The following example demonstrates a client-side call to obtain Digest credentials for a specific user account.


```C++
#include <windows.h>

#ifdef UNICODE
  ClientAuthID.Flags = SEC_WINNT_AUTH_IDENTITY_UNICODE;
#else
  ClientAuthID.Flags = SEC_WINNT_AUTH_IDENTITY_ANSI;
#endif

void main()
{
    SECURITY_STATUS SecStatus; 
    TimeStamp tsLifetime; 
    CredHandle hCred;
    SEC_WINNT_AUTH_IDENTITY ClientAuthID;
    LPTSTR UserName = TEXT("ASecurityPrinciple");
    LPTSTR DomainName = TEXT("AnAuthenticatingDomain");

    // Initialize the memory.
    ZeroMemory( &amp;ClientAuthID, sizeof(ClientAuthID) );

    // Specify string format for the ClientAuthID structure.


    // Specify an alternate user, domain and password.
      ClientAuthID.User = (unsigned char *) UserName;
      ClientAuthID.UserLength = _tcslen(UserName);

      ClientAuthID.Domain = (unsigned char *) DomainName;
      ClientAuthID.DomainLength = _tcslen(DomainName);

    // Password is an application-defined LPTSTR variable
    // containing the user password.
      ClientAuthID.Password = Password;
      ClientAuthID.PasswordLength = _tcslen(Password);

    // Get the client side credential handle.
    SecStatus = AcquireCredentialsHandle (
      NULL,                  // Default principal.
      WDIGEST_SP_NAME,       // The Digest SSP. 
      SECPKG_CRED_OUTBOUND,  // Client will use the credentials.
      NULL,                  // Do not specify LOGON id.
      &amp;ClientAuthID,         // User information.
      NULL,                  // Not used with Digest SSP.
      NULL,                  // Not used with Digest SSP.
      &amp;hCred,                // Receives the credential handle.
      &amp;tsLifetime            // Receives the credential time limit.
    );
}
```



The **\_tcslen** function returns the string length in characters, not including the terminating null character.

If your application can use the credentials established at logon, see [Obtaining Default Digest Credentials](obtaining-default-digest-credentials.md).

 

 



