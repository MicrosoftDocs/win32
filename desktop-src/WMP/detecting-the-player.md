---
title: Detecting the Player
description: Detecting the Player
ms.assetid: dc034226-578a-45de-9463-e1798fef874e
keywords:
- Windows Media Player online stores,detecting players
- online stores,detecting players
- type 1 online stores,detecting players
- type 2 online stores,detecting players
- Windows Media Player online stores,player detection
- online stores,player detection
- type 1 online stores,player detection
- type 2 online stores,player detection
- player detection
- detecting players
ms.topic: article
ms.date: 05/31/2018
---

# Detecting the Player

When creating a webpage for your online store, you may decide that you want users to be able to view the page in a Web browser or in Windows Media Player. You can use an ASP script to determine whether your webpage is hosted in the Player.

The following example code retrieves the version parameter from the URL query string to determine whether the page is hosted in Windows Media Player:


```C++
<%
    Dim sVersion

    sVersion = Trim(Request.QueryString("version")) 
 
    If sVersion = "" Then   
        Response.Write "Not hosted in Windows Media Player"
    Else 
        Response.Write "Hosted in Windows Media Player<BR>"
        Response.Write "Version is " & sVersion
    End If
%>
```



Note that the preceding code assumes that the version parameter exists in the query string when hosted in Windows Media Player. This is true for pages opened by the user, but may not be true for pages opened by using **External.NavigateTaskPaneURL**. For the version query string to exist when navigating programmatically, you must add the version parameter to the method call or dynamically append the version to the base URL of the **Navigate** element of your ServiceInfo document.

## Related topics

<dl> <dt>

[**Creating the ServiceInfo Document Dynamically**](creating-the-serviceinfo-document-dynamically.md)
</dt> <dt>

[**External.NavigateTaskPaneURL**](external-navigatetaskpaneurl.md)
</dt> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> </dl>

 

 




