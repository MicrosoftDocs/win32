---
description: The Class table contains COM server-related information that must be generated as a part of the product advertisement. Each row may generate a set of registry keys and values. The associated ProgId information is included in this table.
ms.assetid: 0fa00a3f-2a5d-411d-9fc6-9486a600f018
title: Class Table
ms.topic: article
ms.date: 05/31/2018
---

# Class Table

The Class table contains COM server-related information that must be generated as a part of the product advertisement. Each row may generate a set of registry keys and values. The associated ProgId information is included in this table.

The Class table has the following columns.



| Column           | Type                         | Key | Nullable |
|------------------|------------------------------|-----|----------|
| CLSID            | [GUID](guid.md)             | Y   | N        |
| Context          | [Identifier](identifier.md) | Y   | N        |
| Component\_      | [Identifier](identifier.md) | Y   | N        |
| ProgId\_Default  | [Text](text.md)             | N   | Y        |
| Description      | [Text](text.md)             | N   | Y        |
| AppId\_          | [GUID](guid.md)             | N   | Y        |
| FileTypeMask     | [Text](text.md)             | N   | Y        |
| Icon\_           | [Identifier](identifier.md) | N   | Y        |
| IconIndex        | [Integer](integer.md)       | N   | Y        |
| DefInprocHandler | [Filename](filename.md)     | N   | Y        |
| Argument         | [Formatted](formatted.md)   | N   | Y        |
| Feature\_        | [Identifier](identifier.md) | N   | N        |
| Attributes       | [Integer](integer.md)       | N   | Y        |



 

## Column Information

<dl> <dt>

<span id="CLSID"></span><span id="clsid"></span>CLSID
</dt> <dd>

The Class identifier (ID) of a COM server.

</dd> <dt>

<span id="Context"></span><span id="context"></span><span id="CONTEXT"></span>Context
</dt> <dd>

The server context for this server. Enter one of the following values for the CLSID Key.



| CLSID KEY                             | Description                                                               |
|---------------------------------------|---------------------------------------------------------------------------|
| [LocalServer](../com/localserver.md)       | Specifies the full path to a 16-bit local server application.             |
| [LocalServer32](../com/localserver32.md)   | Specifies the full path to a 32-bit local server application.             |
| [InprocServer](../com/inprocserver.md)     | Specifies the path to an in-process server DLL.                           |
| [InprocServer32](../com/inprocserver32.md) | Specifies the path to a 32-bit in-process server and the threading model. |



 

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key into the [Component table](component-table.md) specifying the component whose key file provides the COM server.

</dd> <dt>

<span id="ProgId_Default"></span><span id="progid_default"></span><span id="PROGID_DEFAULT"></span>ProgId\_Default
</dt> <dd>

The default Program ID associated with this Class ID. This column is a foreign key into the [ProgID table](progid-table.md).

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

Localized description associated with the Class ID and Program ID.

</dd> <dt>

<span id="AppId_"></span><span id="appid_"></span><span id="APPID_"></span>AppId\_
</dt> <dd>

Application ID containing DCOM information for the associated application (string [GUID](guid.md)). This column is a foreign key into the [AppId table](appid-table.md).

</dd> <dt>

<span id="FileTypeMask"></span><span id="filetypemask"></span><span id="FILETYPEMASK"></span>FileTypeMask
</dt> <dd>

Contains information for the HKCR (this CLSID) key.

If multiple patterns exist, they must be delimited by a semicolon, and numeric subkeys are generated: 0, 1, 2... For more information about this functionality, see [**GetClassFile**](/windows/win32/api/objbase/nf-objbase-getclassfile).

</dd> <dt>

<span id="Icon_"></span><span id="icon_"></span><span id="ICON_"></span>Icon\_
</dt> <dd>

The file providing the icon associated with this CLSID. The installer writes the entry in this column under the DefaultIcon key associated with the ProgId. If it is not null, the column is a foreign key into the [Icon table](icon-table.md). If it is null, the COM server provides the icon resource. Advertised file associations and shortcuts require a non-null value in this column to display properly.

</dd> <dt>

<span id="IconIndex"></span><span id="iconindex"></span><span id="ICONINDEX"></span>IconIndex
</dt> <dd>

Icon index into the icon file. This can be null.

Non-negative numbers only.

</dd> <dt>

<span id="DefInprocHandler"></span><span id="definprochandler"></span><span id="DEFINPROCHANDLER"></span>DefInprocHandler
</dt> <dd>

This field specifies the default in-process handler for the server context specified in the Context field.

This field must be Null if an InprocServer or InprocServer CLSID key appears in the Context field.

If a LocalServer or LocalServer32 CLSID key appears in the Context field, the value in the DefInprocHandler field identifies the default in-process handler.



| Value                | Description                                                                                                                                                                                                                                                                       |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| non-numeric value    | The installer treats a non-numeric value in the DefInprocHandler field as a system file serving as the 32-bit in-process handler specified by the InprocHandler32 key.                                                                                                            |
| Null                 | The DefInprocHandler and Argument fields can both be Null for a LocalServer or LocalServer32 CLSID key.                                                                                                                                                                           |
| 1 = default (system) | The default is the 16-bit in-process handler specified by InprocHandler. In this case, the value of InprocHandler is the name in the registry under which the value of the default in-process handler is stored. For example, HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\CLSID.     |
| 2 = default (system) | The default is the 32-bit in-process handler specified by InprocHandler32. In this case, the value of InprocHandler32 is the name in the registry under which the value of the default in-process handler is stored. For example, HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\CLSID. |
| 3 = default (system) | The default is a 16-bit or 32-bit in-process handler.                                                                                                                                                                                                                             |



 

</dd> <dt>

<span id="Argument"></span><span id="argument"></span><span id="ARGUMENT"></span>Argument
</dt> <dd>

If a LocalServer or LocalServer32 CLSID key appears in the Context field, the text in this field is registered as the argument against the server and is used by COM to invoke the server. The DefInprocHandler and Argument fields can both be Null if LocalServer or LocalServer32 appears in the Context field.

Note that the resolution of properties in the Argument field is limited. A property formatted as \[Property\] in this field can only be resolved if the property already has the intended value when the component owning the class is installed. For example, for the argument "\[\#MyDoc.doc\]" to resolve to the correct value, the same process must be installing the file MyDoc.doc and the component that owns the class.

</dd> <dt>

<span id="Feature_"></span><span id="feature_"></span><span id="FEATURE_"></span>Feature\_
</dt> <dd>

External key into the [Feature table](feature-table.md) specifying the feature that provides the COM server.

External key to column one of the Feature table.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

If **msidbClassAttributesRelativePath** is set in this column, the bare file name can be used for COM servers. The installer registers the file name only instead of the complete path. This enables the server in the current directory to take precedence and allows multiple copies of the same component.



| Attribute                            | Decimal | Hexadecimal |
|--------------------------------------|---------|-------------|
| **msidbClassAttributesRelativePath** | 1       | 0x001       |



 

</dd> </dl>

## Remarks

This table is referred to when the [RegisterClassInfo action](registerclassinfo-action.md) or the [UnregisterClassInfo action](unregisterclassinfo-action.md) are executed.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE19](ice19.md)  
[ICE32](ice32.md)  
[ICE36](ice36.md)  
[ICE41](ice41.md)  
[ICE42](ice42.md)  
[ICE46](ice46.md)  
[ICE66](ice66.md)  
[ICE69](ice69.md)  
</dl>

 

 
