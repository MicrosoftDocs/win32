---
Description: Setting Up the Form (.Htm File)
ms.assetid: 9ab712bf-7c36-41f0-ba05-172810a8e6ab
title: Setting Up the Form (.Htm File)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting Up the Form (.Htm File)

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following example shows a basic query form.

**To create a basic query form as in the example**

1.  Type the following HTML code in a file.
    ```
    <HTML>
    <HEAD>
        <TITLE>Indexing Service Search Form</TITLE>
    </HEAD> 
    <BODY> 
    <FORM ACTION="ixtourqy.idq" METHOD="GET"> 
    Search for: 
    <INPUT TYPE="TEXT" NAME="CiRestriction" SIZE="30" MAXLENGTH="100" VALUE="">
    <INPUT TYPE="SUBMIT" VALUE="Execute Query">
    <INPUT TYPE="RESET" VALUE="Clear"> 
    </FORM> 
    </BODY>
    </HTML>
    ```

    

2.  Save the file in HTML format.

The two most important lines of HTML code are:


```
<FORM ACTION. . .>
```



Tells where to find the .idq file that goes with this form. Because an .idq file helps process an Indexing Service query form, every Indexing Service query form must specify a corresponding .idq file.


```
<INPUT TYPE="TEXT". . .>
```



Defines a variable called *CiRestriction*. This variable is preset to accept whatever text is typed into the query field (the **Search for** field, in the example). For example, if you type *cache* in this field, *CiRestriction* holds the text cache.

When the **Execute Query** button is clicked, the data in the text field is sent to IIS and processed. IIS finds the specified .idq file and passes the query data and the .idq file to Indexing Service. To learn how to construct complex queries, see [Query Languages for Indexing Service](query-languages-for-indexing-service.md).

 

 



