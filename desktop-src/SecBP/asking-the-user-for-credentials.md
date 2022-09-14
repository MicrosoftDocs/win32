---
description: Your application may need to prompt the user for user name and password information to avoid storing an administrator password or to verify that the token holds the appropriate privileges.
ms.assetid: 966de0cc-63de-4430-843f-668de2dfe0a6
title: Asking the User for Credentials
ms.topic: article
ms.date: 05/31/2018
---

# Asking the User for Credentials

Your application may need to prompt the user for user name and password information to avoid storing an administrator password or to verify that the token holds the appropriate privileges.

However, simply prompting for credentials may train users to supply those to any random, unidentified dialog box that appears on the screen. The following procedure is recommended to reduce that training effect.

**To properly acquire user credentials**

1.  Inform the user, by using a message that is clearly part of your application, that they will see a dialog box that requests their user name and password. You can also use the [**CREDUI\_INFO**](/windows/desktop/api/wincred/ns-wincred-credui_infoa) structure on the call to [**CredUIPromptForCredentials**](/windows/desktop/api/wincred/nf-wincred-creduipromptforcredentialsa) to convey identifying data or a message.
2.  Call [**CredUIPromptForCredentials**](/windows/desktop/api/wincred/nf-wincred-creduipromptforcredentialsa). Note that the maximum number of characters specified for user name and password information includes the terminating null character.
3.  Call [**CredUIParseUserName**](/windows/desktop/api/wincred/nf-wincred-creduiparseusernamea) and [**CredUIConfirmCredentials**](/windows/desktop/api/wincred/nf-wincred-creduiconfirmcredentialsa) to verify that you obtained appropriate credentials.

The following example shows how to call [**CredUIPromptForCredentials**](/windows/desktop/api/wincred/nf-wincred-creduipromptforcredentialsa) to ask the user for a user name and password. It begins by filling in a CREDUI\_INFO structure with information about what prompts to use. Next, the code fills two buffers with zeros. This is done to ensure that no information gets passed to the function that might reveal an old user name or password to the user. The call to **CredUIPromptForCredentials** brings up the dialog box. For security reasons, this example uses the CREDUI\_FLAGS\_DO\_NOT\_PERSIST flag to prevent the operating system from storing the password because it might then be exposed. If there are no errors, **CredUIPromptForCredentials** fills in the pszName and pszPwd variables and returns zero. When the application has finished using the credentials, it should put zeros in the buffers to prevent the information from being accidentally revealed.


```C++
CREDUI_INFO cui;
TCHAR pszName[CREDUI_MAX_USERNAME_LENGTH+1];
TCHAR pszPwd[CREDUI_MAX_PASSWORD_LENGTH+1];
BOOL fSave;
DWORD dwErr;
 
cui.cbSize = sizeof(CREDUI_INFO);
cui.hwndParent = NULL;
//  Ensure that MessageText and CaptionText identify what credentials
//  to use and which application requires them.
cui.pszMessageText = TEXT("Enter administrator account information");
cui.pszCaptionText = TEXT("CredUITest");
cui.hbmBanner = NULL;
fSave = FALSE;
SecureZeroMemory(pszName, sizeof(pszName));
SecureZeroMemory(pszPwd, sizeof(pszPwd));
dwErr = CredUIPromptForCredentials( 
    &cui,                         // CREDUI_INFO structure
    TEXT("TheServer"),            // Target for credentials
                                  //   (usually a server)
    NULL,                         // Reserved
    0,                            // Reason
    pszName,                      // User name
    CREDUI_MAX_USERNAME_LENGTH+1, // Max number of char for user name
    pszPwd,                       // Password
    CREDUI_MAX_PASSWORD_LENGTH+1, // Max number of char for password
    &fSave,                       // State of save check box
    CREDUI_FLAGS_GENERIC_CREDENTIALS |  // flags
    CREDUI_FLAGS_ALWAYS_SHOW_UI |
    CREDUI_FLAGS_DO_NOT_PERSIST);  

if(!dwErr)
{
    //  Put code that uses the credentials here.
 
    //  When you have finished using the credentials,
    //  erase them from memory.
    SecureZeroMemory(pszName, sizeof(pszName));
    SecureZeroMemory(pszPwd, sizeof(pszPwd));
}
```



## Related topics

<dl> <dt>

[**CredUICmdLinePromptForCredentials**](/windows/desktop/api/wincred/nf-wincred-creduicmdlinepromptforcredentialsa)
</dt> <dt>

[**CREDUI\_UINFO**](/windows/desktop/api/wincred/ns-wincred-credui_infoa)
</dt> </dl>

 

 
