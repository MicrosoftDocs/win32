---
title: DIFsrmClassificationEvents OnFile event
description: Receives properties of files that are processed by ClassifyFiles.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12218681-e986-4798-befe-59b999d6b473
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- OnFile event File Server Resource Manager
- OnFile event File Server Resource Manager , DIFsrmClassificationEvents interface
- DIFsrmClassificationEvents interface File Server Resource Manager , OnFile event
topic_type:
- apiref
api_name:
- DIFsrmClassificationEvents.OnFile
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DIFsrmClassificationEvents::OnFile event

The **OnFile** event handler method receives properties of files that are returned in a call to [**ClassifyFiles**](/windows/previous-versions/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager2-classifyfiles?branch=master).

## Syntax


```C++
HRESULT OnFile(
  [in]                   BSTR            filePath,
  [in]                   HRESULT         result,
  [in]                   BSTR            fileMessages,
  [in, optional, unique] IFsrmCollection *fileProperties,
  [out, retval]          VARIANT_BOOL    *ret
);
```



## Parameters

<dl> <dt>

*filePath* \[in\]
</dt> <dd>

Path of file.

</dd> <dt>

*result* \[in\]
</dt> <dd>

Return value for the specific file. If this value is an error code then the *fileProperties* parameter may be **NULL**.

</dd> <dt>

*fileMessages* \[in\]
</dt> <dd>

Message specific to any error.

</dd> <dt>

*fileProperties* \[in, optional\]
</dt> <dd>

Address of a [**IFsrmCollection**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmcollection?branch=master) that contains the set of properties set on the file.

</dd> <dt>

*ret* \[out, retval\]
</dt> <dd>

Address of a **VARIANT\_BOOL**. Set this to **VARIANT\_FALSE** to cancel the classification. [**ClassifyFiles**](/windows/previous-versions/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager2-classifyfiles?branch=master) will then fail with **FSRM\_E\_CLASSIFICATION\_CANCELED**.

</dd> </dl>

## Return value

The event handler method returns **S\_OK** if there were no errors processing the event. Any error values will cancel the operation and be passed to [**ClassifyFiles**](/windows/previous-versions/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager2-classifyfiles?branch=master). The error should indicate the source of the failure (for example **E\_OUTOFMEMORY** if an allocation failed.) For a list of common error codes, see [**COM Error Codes (Generic)**](https://msdn.microsoft.com/library/windows/desktop/dd542643).

## Examples

For an example that demonstrates this method see [Classifying Files](classifying-files.md).

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Type library<br/>             | <dl> <dt>Srm.dll</dt> </dl>             |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>          |
| IID<br/>                      | DIID\_DIFsrmClassificationEvents is defined as 26942db0-dabf-41d8-bbdd-b129a9f70424<br/> |



## See also

<dl> <dt>

[**DIFsrmClassificationEvents**](/windows/previous-versions/FsrmTlb/?branch=master)
</dt> <dt>

[**IFsrmClassificationManager2::ClassifyFiles**](/windows/previous-versions/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager2-classifyfiles?branch=master)
</dt> </dl>

 

 





