---
Description: Sets or retrieves the CAPICOM name of the attribute. This is the default property.
ms.assetid: 082f286e-f2ac-4e45-94b9-abdaa3f4c926
title: Attribute.Name property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Attribute.Name property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**CryptographicAttributeObject Class**](https://www.bing.com/search?q=**CryptographicAttributeObject+Class**) in the [**System.Security.Cryptography**](https://www.bing.com/search?q=**System.Security.Cryptography**) namespace.\]

The **Name** property sets or retrieves the CAPICOM name of the attribute. This is the default property.

This property is read/write.

## Syntax


```VB
Attribute.Name As CAPICOM_ATTRIBUTE
```



## Property value

A value of the [**CAPICOM\_ATTRIBUTE**](capicom-attribute.md) enumeration that specifies the CAPICOM name of the attribute. The following table shows the possible values.



| Value                                                                                                                                                                                                                                                                                 | Meaning                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <span id="CAPICOM_AUTHENTICATED_ATTRIBUTE_SIGNING_TIME"></span><span id="capicom_authenticated_attribute_signing_time"></span><dl> <dt>**CAPICOM\_AUTHENTICATED\_ATTRIBUTE\_SIGNING\_TIME**</dt> </dl>                         | The attribute contains the time that the signature was created.<br/> |
| <span id="CAPICOM_AUTHENTICATED_ATTRIBUTE_DOCUMENT_NAME"></span><span id="capicom_authenticated_attribute_document_name"></span><dl> <dt>**CAPICOM\_AUTHENTICATED\_ATTRIBUTE\_DOCUMENT\_NAME**</dt> </dl>                      | The attribute contains the name of the signed document.<br/>         |
| <span id="CAPICOM_AUTHENTICATED_ATTRIBUTE_DOCUMENT_DESCRIPTION"></span><span id="capicom_authenticated_attribute_document_description"></span><dl> <dt>**CAPICOM\_AUTHENTICATED\_ATTRIBUTE\_DOCUMENT\_DESCRIPTION**</dt> </dl> | The attribute contains a description of the signed document.<br/>    |



 

## Remarks

When the value of this property is reset, directly or indirectly, the whole state of the object is reset.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Attribute**](attribute.md)
</dt> </dl>

 

 




