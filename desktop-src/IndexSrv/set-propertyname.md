---
title: SET PROPERTYNAME
description: SET PROPERTYNAME
ms.assetid: edd966ed-ae5f-47a8-888a-5177cdef76b3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SET PROPERTYNAME

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **SET PROPERTYNAME** statement associates a property set with a friendly name (column alias) and a data type for the duration of an active connection. The property is identified by a GUID and a property ID, which can be either a number or a string.

``` syntax
SET PROPERTYNAME 'GUID' PROPID {'Property_Name' | Property_ID}
    AS Friendly_Name [TYPE dbtype]
```

### Parameters

<dl> <dt>

<span id="GUID"></span><span id="guid"></span>*GUID*
</dt> <dd>

Specifies the globally unique identifier (GUID). The GUID must be written in the following format, enclosed in single quotes:

-   One 8-hex-character sequence, followed by a minus sign
-   Three 4-hex-character sequences, each followed by a minus sign
-   One 12-hex-character sequence

</dd> <dt>

<span id="Property_Name"></span><span id="property_name"></span><span id="PROPERTY_NAME"></span>*Property\_Name*
</dt> <dd>

Specifies the name of the property within the ActiveX property namespace.

</dd> <dt>

<span id="Property_ID"></span><span id="property_id"></span><span id="PROPERTY_ID"></span>*Property\_ID*
</dt> <dd>

Specifies the property ID as a decimal or hexadecimal number. If you use a hexadecimal number, precede the number with "0x".

</dd> <dt>

<span id="Friendly_Name"></span><span id="friendly_name"></span><span id="FRIENDLY_NAME"></span>*Friendly\_Name*
</dt> <dd>

Specifies the friendly name (column alias). It is possible to set different (multiple) friendly names to the same property. For example, the friendly name "author" may be also known as "auteur" in a community where both English and French are spoken. However, it is important to note that these two friendly names cannot be used in the same query.

</dd> <dt>

<span id="dbtype"></span><span id="DBTYPE"></span>*dbtype*
</dt> <dd>

Specifies the type of data being used. The *dbtype* parameter is optional for Indexing Service. You need to specify the parameter in situations when the data type is not a string, which is the default. For example, in the following piece of code, Indexing Service needs to know whether to interpret the value as a string or a date:


```
WHERE MyProperty = '1996-10-10'
```



If the data type is not provided, **DBTYPE\_WSTR** (Unicode string) is assumed. See [Names Section of .Idq Files](names-section-of-idq-files.md) for further information.

</dd> </dl>

### Remarks

After a property name has been used in a view, it cannot be redefined.

### Example

The following is an example of the **SET PROPERTYNAME** statement.


```
SET PROPERTYNAME 'D5CDD502-2E9C-101B-9397-08002B2CF9AE'  PROPID 0xE AS DocManager
```



## Related topics

<dl> <dt>

[SET RANKMETHOD](set-rankmethod.md)
</dt> <dt>

[SET Statement](set-statement.md)
</dt> </dl>

 

 




