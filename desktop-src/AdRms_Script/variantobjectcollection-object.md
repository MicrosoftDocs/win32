---
Description: Contains abstract methods and properties that manage a generic collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 30a5e8ba-e5e0-4e25-8942-ce7dc87959c8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: VariantObjectCollection object
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# VariantObjectCollection object

The **VariantObjectCollection** object contains abstract methods and properties that manage a generic collection. This object is inherited by the following objects:

-   [**ApplicationSpecificDataItemCollection**](applicationspecificdataitemcollection-object.md)
-   [**ExcludedApplicationCollection**](excludedapplicationcollection-object.md)
-   [**ExcludedUserAccountCollection**](excludeduseraccountcollection-object.md)
-   [**RightsTemplateCollection**](rightstemplatecollection-object.md)
-   [**StringCollection**](stringcollection-object.md)
-   [**TemplateLocaleNameCollection**](templatelocalenamecollection-object.md)
-   [**TemplateSummaryCollection**](templatesummarycollection-object.md)
-   [**TrustedPublishingDomainCollection**](trustedpublishingdomaincollection-object.md)
-   [**TrustedUserDomainCollection**](trusteduserdomaincollection-object.md)
-   [**UserRightsItemCollection**](userrightsitemcollection-object.md)

## Members

The **VariantObjectCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **VariantObjectCollection** object has these methods.



| Method                                                     | Description                                                                                                                                                          |
|:-----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Add](http://go.microsoft.com/fwlink/p/?linkid=87269)      | Adds an object to the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                                |
| [Clear](http://go.microsoft.com/fwlink/p/?linkid=87270)    | Removes all objects from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                         |
| [Contains](http://go.microsoft.com/fwlink/p/?linkid=87271) | Determines whether the collection contains a specific object (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                    |
| [CopyTo](http://go.microsoft.com/fwlink/p/?linkid=87281)   | Copies the collection elements to an array, starting at a specified index (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [IndexOf](http://go.microsoft.com/fwlink/p/?linkid=87273)  | Retrieves the index of a specific object in the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Insert](http://go.microsoft.com/fwlink/p/?linkid=87274)   | Inserts an object in the collection at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Remove](http://go.microsoft.com/fwlink/p/?linkid=87276)   | Removes the first occurrence of the specified object from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>        |
| [RemoveAt](http://go.microsoft.com/fwlink/p/?linkid=87277) | Removes the object at the specified index from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                   |



 

### Properties

The **VariantObjectCollection** object has these properties.



| Property                                                           | Description                                                                                                                                            |
|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Count](http://go.microsoft.com/fwlink/p/?linkid=87280)<br/> | Retrieves the number of objects contained in the collection (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [Item](http://go.microsoft.com/fwlink/p/?linkid=87278)<br/>  | Specifies or retrieves the object at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>          |



 

## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




