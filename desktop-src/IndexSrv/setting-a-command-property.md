---
title: Setting a Command Property
description: Setting a Command Property
ms.assetid: eddc827b-929e-42ee-a81f-c4e0c96d1bcf
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting a Command Property

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following example demonstrates how to set an OLE DB property for the [**ICommand**](089427ad-5ba3-4613-b89e-8e86420ccc30) interface. The example declares the **SetUseContentIndex** function, which sets Indexing Service's [**DBPROP\_USECONTENTINDEX**](dbprop-usecontentindex.md) property to VARIANT\_TRUE.


```
HRESULT SetUseContentIndex( ICommand * pICommand )
{
  static const DBID dbcolNull = { {0,0,0,{0,0,0,0,0,0,0,0}},DBKIND_GUID_PROPID,0 };
  static const GUID guidQueryExt = DBPROPSET_QUERYEXT;
 
  DBPROP aProp[1];
  aProp[0].dwPropertyID = DBPROP_USECONTENTINDEX;
  aProp[0].dwOptions = DBPROPOPTIONS_SETIFCHEAP;
  aProp[0].dwStatus = 0;
  aProp[0].colid = dbcolNull;
  aProp[0].vValue.vt = VT_BOOL;
  aProp[0].vValue.boolVal = VARIANT_TRUE;
 
  DBPROPSET aPropSet[1];
  aPropSet[0].rgProperties = &amp;aProp[0];
  aPropSet[0].cProperties = 1;
  aPropSet[0].guidPropertySet = guidQueryExt;
 
  ICommandProperties * pICommandProperties;
  HRESULT hr = pICommand->QueryInterface( IID_ICommandProperties,
                                          (IUnknown **) &amp;pICommandProperties );
  if ( FAILED( hr ) )
    return hr;
 
  hr = pICommandProperties->SetProperties( 1, aPropSet );
  pICommandProperties->Release();
 
  return hr;
}
```



 

 




