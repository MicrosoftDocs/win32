---
title: ITfContextRenderingMarkup interface
description: The ITfContextRenderingMarkup interface is implemented by TSF manager and used by applications. This interface can be retrieved using IQueryInterface from ITfContext object. This interface helps the application enumerate rendering information.
ms.assetid: 733d2db2-f9e9-4b78-af13-adc03825bf2b
keywords:
- ITfContextRenderingMarkup interface Text Services Framework
- ITfContextRenderingMarkup interface Text Services Framework , described
topic_type:
- apiref
api_name:
- ITfContextRenderingMarkup
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ITfContextRenderingMarkup interface

The **ITfContextRenderingMarkup** interface is implemented by TSF manager and used by applications. This interface can be retrieved using IQueryInterface from [ITfContext](/windows/desktop/api/Msctf/nn-msctf-itfcontext) object. This interface helps the application enumerate rendering information.



| ITfContextRenderingMarkup methods                                                | Description                                                           |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [GetRenderingMarkup](itfcontextrenderingmarkup-getrenderingmarkup.md)           | Retrieves an enumerator of the rendering markups for the given range. |
| [FindNextRenderingMarkup](itfcontextrenderingmarkup-findnextrenderingmarkup.md) | This function is not implemented. It always returns E\_NOTIMPL.       |



 

## Members

The **ITfContextRenderingMarkup** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Remarks

> [!Note]  
> This interface is not currently in the public header files. To use this API, you must MIDL-compile the [prototype](prototypes.md).

 

 

 