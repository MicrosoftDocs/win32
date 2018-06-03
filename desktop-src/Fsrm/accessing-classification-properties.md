---
title: Accessing Classification Properties
description: Enumerating FSRM classification properties is easily done using the FsrmClassificationManager object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E057898F-72A0-4AB0-BE88-4C1BE6B2B5DE
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Classification Properties

Enumerating FSRM classification properties is easily done using the [**FsrmClassificationManager**](/previous-versions/windows/desktop/api/FsrmTlb/) object.

All interfaces required to access and manage properties are defined in SrmLib.dll found in the System32 directory of Windows Server 2008 R2 and later. This library will have to be added as a reference to projects that attempt to interface with the classification infrastructure. All the relevant interfaces are in the **Microsoft.Storage** namespace.

-   [Querying classification property definitions](#querying-classification-property-definitions)
-   [Retrieving a classification property by name](#retrieving-a-classification-property-by-name)
-   [Retrieving classification properties on a file](#retrieving-classification-properties-on-a-file)
-   [Setting a property on a file](#setting-a-property-on-a-file)
-   [Property type representations](#property-type-representations)
-   [Related topics](#related-topics)

## Querying classification property definitions

Querying the classification property definitions on a server has to be done via APIs. It follows this pattern:

-   Create a [**FsrmClassificationManager**](/previous-versions/windows/desktop/api/FsrmTlb/) object.
-   Call the [**EnumPropertyDefinitions**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-enumpropertydefinitions) method of the returned object.
-   Process the collection of [**IFsrmPropertyDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpropertydefinition) objects returned.

This snippet demonstrates enumerating classification properties.


```CSharp
FsrmClassificationManager cls = new FsrmClassificationManager();
 
ICollection c = cls.EnumPropertyDefinitions
(_FsrmEnumOptions.FsrmEnumOptions_None);
foreach (IFsrmPropertyDefinition p in c)
{
/*...*/
}
```

<span codelanguage="PowerShell"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$cls = New-Object -com Fsrm.FsrmClassificationManager
$cls.EnumPropertyDefinitions()</code></pre></td>
</tr>
</tbody>
</table>



## Retrieving a classification property by name

If the name of a property is known, the property definition can be retrieved using the [**GetPropertyDefinition**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-getpropertydefinition) method.

> [!Note]  
> This is the **Name** property of the property definition, not the **DisplayName** property.

 

This snippet demonstrates retrieving a classification property.


```CSharp
FsrmClassificationManager cls = new FsrmClassificationManager();
 
IFsrmPropertyDefinition p = cls.GetPropertyDefinition("<Name>");
```

<span codelanguage="PowerShell"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$cls = New-Object -com Fsrm.FsrmClassificationManager
$cls.GetPropertyDefinition(&quot;&lt;Name&gt;&quot;)</code></pre></td>
</tr>
</tbody>
</table>



## Retrieving classification properties on a file

To query the classification properties on a file there are two mechanisms available:

-   If the name of the property is known, the [**GetFileProperty**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-getfileproperty) method can be used to specify the exact property to get.

    > [!Note]  
    > This is the **Name** property of the property definition, not the **DisplayName** property.

     

-   Otherwise, the [**EnumFileProperties**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-enumfileproperties) method can retrieve all properties known for a file.

In either case, the mechanism to do this follows this pattern:

-   Create a [**FsrmClassificationManager**](/previous-versions/windows/desktop/api/FsrmTlb/) object.
-   Call the [**GetFileProperty**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-getfileproperty) or [**EnumFileProperties**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-enumfileproperties) method on the returned object.

This snippet demonstrates retrieving classification properties on a file.


```CSharp
FsrmClassificationManager cls = new FsrmClassificationManager();
            
/* The _FsrmGetFilePropertyOptions.FsrmGetFilePropertyOptions_None
* option signals that if the file has not been 
* classified yet, any applicable rules should be applied
* to classify the file now.
*/
IFsrmProperty p = cls.GetFileProperty(@"c:\data\data.txt", 
                                      "Business Impact",
                                      _FsrmGetFilePropertyOptions.FsrmGetFilePropertyOptions_None);
if (p.Value == "HBI")
{
/*...*/
}
            
/* The _FsrmGetFilePropertyOptions.FsrmGetFilePropertyOptions_NoRuleEvaluation
* option signals that only properties stored in the 
* cache, or one of the storage modules should be 
* returned. If the file has not been classified yet, no
* properties will be returned.
*/
ICollection c = cls.EnumFileProperties(@"c:\data\data.txt", 
                                      _FsrmGetFilePropertyOptions.FsrmGetFilePropertyOptions_NoRuleEvaluation);
foreach (IFsrmProperty p in c)
{
/*...*/
}
```

<span codelanguage="PowerShell"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$cls = New-Object -com Fsrm.FsrmClassificationManager
$p = $cls.GetFileProperty(&quot;c:\data\data.txt&quot;, &quot;&lt;Name&gt;&quot;, 0)
$c = $cls.EnumFileProperties(&quot;c:\data\data.txt&quot;, &quot;&lt;Name&gt;&quot;, 1)</code></pre></td>
</tr>
</tbody>
</table>



## Setting a property on a file

Setting a property on a file is very similar using the [**SetFileProperty**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-setfileproperty) method.

> [!Note]  
> This is the **Name** property of the fille property, not the **DisplayName** property.

 

This snippet demonstrates setting a property on a file.


```CSharp
FsrmClassificationManager cls = new FsrmClassificationManager();
cls.SetFileProperty(@"c:\data\data.txt", "<Name>", "<Value>");
```

<span codelanguage="PowerShell"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$cls = New-Object -com Fsrm.FsrmClassificationManager
$p = $cls.SetFileProperty(&quot;c:\data\data.txt&quot;, &quot;&lt;Name&gt;&quot;, &quot;&lt;Value&gt;&quot;)</code></pre></td>
</tr>
</tbody>
</table>



## Property type representations

Values for properties are always Unicode strings. The following conventions should be used when retrieving or setting classification properties:



| Property Type           | Unicode String Representation                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------|
| String<br/>       | Standard representation of value<br/>                                                    |
| Integer<br/>      | Standard representation of value<br/>                                                    |
| Ordered List<br/> | Standard representation of value<br/>                                                    |
| Boolean<br/>      | "1" for yes/true and "0" for no/false<br/>                                               |
| Date<br/>         | Standard representation of a decimal 64 bit [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284) value<br/> |
| Multi-choice<br/> | Standard representation of values separated by '\|'<br/>                                 |
| Multi-string<br/> | Standard representation of values separated by '\|'<br/>                                 |



 

## Related topics

<dl> <dt>

[Using FSRM](using-fsrm.md)
</dt> <dt>

[**FsrmClassificationManager**](/previous-versions/windows/desktop/api/FsrmTlb/)
</dt> <dt>

[**IFsrmClassificationManager**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager)
</dt> <dt>

[**IFsrmClassificationManager::EnumFileProperties**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-enumfileproperties)
</dt> <dt>

[**IFsrmClassificationManager::EnumPropertyDefinitions**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-enumpropertydefinitions)
</dt> <dt>

[**IFsrmClassificationManager::GetFileProperty**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-getfileproperty)
</dt> <dt>

[**IFsrmClassificationManager::GetPropertyDefinition**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-getpropertydefinition)
</dt> <dt>

[**IFsrmClassificationManager::SetFileProperty**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager-setfileproperty)
</dt> <dt>

[**IFsrmPropertyDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpropertydefinition)
</dt> </dl>

 

 





