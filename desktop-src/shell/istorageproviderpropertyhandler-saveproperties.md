---
Description: Saves properties associated with a file or folder.
ms.assetid: 983751BA-BF36-4018-A95A-4BEA1E9BA3BF
title: IStorageProviderPropertyHandlerSaveProperties method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IStorageProviderPropertyHandler::SaveProperties method

Saves properties associated with a file or folder.

## Syntax


```C++
HRESULT SaveProperties(
  [in] IPropertyStore *propertiesToSave
);
```



## Parameters

<dl> <dt>

*\*propertiesToSave* \[in\]
</dt> <dd>

The properties to save.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Attempting to save properties that are not managed by the sync engine should result in the error code **E\_INVALIDARG**.

## See also

<dl> <dt>

[**IStorageProviderPropertyHandler**](/windows/win32/storageprovider/nn-storageprovider-istorageproviderpropertyhandler?branch=master)
</dt> </dl>

 

 



