---
title: SyncURL Method
description: Use the SyncURL method to select the contents (.hhc) file entry for a topic that you specify.
ms.assetid: 'A8E214B3-8F40-4158-A999-76C5F075533A'
---

# SyncURL Method

Use the SyncURL method to select the contents (.hhc) file entry for a topic that you specify.

The instance of the HTML Help ActiveX control that you reference when using the SyncURL method must specify the [Contents](contents.md) command.

This command can be used only with a compiled help (.chm) file.

Applies to: [Contents](contents.md)

## Syntax

``` syntax
SyncURL(BSTR <i>pszUrl</i>) 
```

## Parameter

<dl> <dt>

<span id="pszUrl_"></span><span id="pszurl_"></span><span id="PSZURL_"></span>*pszUrl* 
</dt> <dd>

Specifies the topic whose corresponding contents entry you want to select.

</dd> </dl>

## Example

The following example shows how to use the SyncURL method to select entries in a contents (.hhc) file.

The code for the control:


```
<OBJECT
   id=sync
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="hhctrl.ocx#Version=5,02,3790,1194"
   width=35%
   height=25%
>
   <PARAM name="Command" value="Contents">
   <PARAM name="Item1" value="methods.hhc">
   </OBJECT>
```



The JavaScript code to invoke the control:


```
<a href=JavaScript:sync.syncURL('textpopup.htm')>Go to textpopup.htm</a> 
```



## Remarks

The SyncURL method provides the same functionality as clicking the **Locate** button on the HTML Help Viewer toolbar.

## Related topics

<dl> <dt>

[About Methods](about-methods.md)
</dt> </dl>

 

 




