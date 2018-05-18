---
title: Setting the Locale and Other Properties
description: Setting the Locale and Other Properties
ms.assetid: 'e6f50d7e-f728-4b2d-b3a8-a6f710dcf1f1'
---

# Setting the Locale and Other Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

To use the ADO API, a program or script often needs to set various dynamic ADO properties of the **Command**, **Connection**, and **Recordset** objects. For a listing of all ADO dynamic properties available for Indexing Service, see [Dynamic ADO Properties](dynamic-ado-properties.md). The remainder of this topic uses, as an example, setting the locale.

You can change the locale for a **Command** object by setting the dynamic ADO property "SQL Content Query Locale String" to the appropriate string. Alternatively, you can set the dynamic ADO property "Locale Identifier" of the **Connection** object to the appropriate locale identifier (LCID).

The following examples illustrate setting the locale for queries.

-   The following example sets the "SQL Content Query Locale String" property of the **Command** object **AdoCommand** to the locale "GE".
    ```
    AdoCommand.Properties("SQL Content Query Locale String") = "GE"
    ```

    

-   The following example obtains the default locale from the browser HTTP\_ACCEPT\_LANGUAGE variable and uses it to set the locale.
    ```
    strLocale = Request.ServerVariable("HTTP_ACCEPT_LANGUAGE")
    AdoCommand.Properties("SQL Content Query Locale String") = strLocale 
    ```

    

-   The following example sets the "Locale Identifier" property of the **Connection** object AdoConnection to the US-English locale.
    ```
    AdoConnection.Properties("Locale Identifier") = 1033 'EN-US locale code
    ```

    

> [!Note]  
> The **Locale** property that you set, in either a **Connection** or **Command** object, does not affect the displayed error messages. The displayed error messages are based on the default locale specified in the user profile. The **Locale** property that you set is passed to Indexing Service, which uses it for searching.

 

 

 




