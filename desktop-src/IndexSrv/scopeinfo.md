---
Description: ScopeInfo
ms.assetid: 64185b3e-efb9-4c7f-a169-acdb7d3739e5
title: ScopeInfo
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScopeInfo

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ScopeInfo** form specifies several scope properties for a new scope of a catalog. This form appears when creating a new directory using the [AdminCatalog](admincatalog.md) form. The **ScopeInfo** form contains the following controls.

-   A text box for the path of the scope.
-   A text box for the login name for the scope.
-   A text box for the password for the scope.
-   A check box that specifies excluding the path from the catalog.
-   A command button to set the specified properties.
-   A command button to cancel the action.

This code segment uses the **GetCatalogByName** method of the gCiAdmin **AdminIndexServer** object to create CiCatalog, a [**CatAdm**](icatadm.md) object. It then uses the **AddScope** method of the CiCatalog **CatAdm** object to add the scope properties from the form to the catalog.


```VB
Private Sub Ok_Click()
...
    Dim CiCatalog As Object

    Set CiCatalog = ISAdminForm.gCiAdmin.GetCatalogByName(Tag)

    Dim vLogon As Variant
    Dim vPassword As Variant

    vLogon = strLogon.Text
    vPassword = strPassword.Text

    CiCatalog.AddScope strPath, fExcludeScope.Value, vLogon, vPassword
...
End Sub
```



 

 



