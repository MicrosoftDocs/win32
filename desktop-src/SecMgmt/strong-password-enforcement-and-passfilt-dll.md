---
description: Lists the requirements enforced by strong password system administration tools.
ms.assetid: a84f83b2-181b-4f65-82bd-bc7f0689aad3
title: Strong Password Enforcement and Passfilt.dll
ms.topic: article
ms.date: 05/31/2018
---

# Strong Password Enforcement and Passfilt.dll

Strong password enforcement can be enabled by using the system administration tools. If the system administration policy is enabled, passwords must meet the following minimum requirements when they are created or changed:

-   Passwords may not contain the user's samAccountName (Account Name) value or entire displayName (Full Name value). Both checks are not case sensitive.
-   The samAccountName is checked in its entirety only to determine whether it is part of the password. If the samAccountName is less than three characters long, this check is skipped.
-   The displayName is parsed for delimiters: commas, periods, dashes or hyphens, underscores, spaces, pound signs, and tabs. If any of these delimiters are found, the displayName is split and all parsed sections (tokens) are confirmed to not be included in the password. Tokens that are less than three characters are ignored, and substrings of the tokens are not checked. For example, the name "Erin M. Hagens" is split into three tokens: "Erin", "M", and "Hagens". Because the second token is only one character long, it is ignored. Therefore, this user could not have a password that included either "erin" or "hagens" as a substring anywhere in the password.
-   Passwords must contain characters from three of the five following categories.



| Character categories                                                                                                                                                      | Examples                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Uppercase letters of European languages (A through Z, with diacritic marks, Greek and Cyrillic characters)<br/>                                                     | A, B, C,   Z<br/>                |
| Lowercase letters of European languages (a through z, sharp-s, with diacritic marks, Greek and Cyrillic characters)<br/>                                            | a, b, c,   z<br/>                |
| Base 10 digits (0 through 9)<br/>                                                                                                                                   | 0, 1, 2,   9<br/>                |
| Non-alphanumeric characters (special characters)<br/>                                                                                                               | $,!,%,^,(){}\[\];:<>?<br/> |
| Any Unicode character that is categorized as an alphabetic character but is not uppercase or lowercase. This includes Unicode characters from Asian languages.<br/> |                                        |



 

**To enable strong password enforcement**

1.  From the administration console, locate **Local Security Policy**.
2.  Select **Account Policy**, and then select **Password Policy**.
3.  Enable the **Passwords must meet complexity requirements** setting.

> [!Note]  
> A given character can satisfy only one category. The [GetStringTypeW](/windows/win32/api/stringapiset/nf-stringapiset-getstringtypew) function is used to test whether each character in the password is uppercase, lowercase, or alphanumeric.

 

 

