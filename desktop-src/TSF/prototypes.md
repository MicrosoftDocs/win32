---
title: Prototypes
description: Prototypes
ms.assetid: 2b31c01b-d52b-4df5-9cb0-a35286febd3a
keywords:
- Text Services Framework (TSF),prototypes
- TSF (Text Services Framework),prototypes
- TSF reference,prototypes
- reference for TSF,prototypes
- text services,prototypes
- TSF-enabled applications,prototypes
- prototypes
ms.topic: article
ms.date: 05/31/2018
---

# Prototypes

[ITfContextRenderingMarkup](/windows/desktop/TSF/itfcontextrenderingmarkup), [IEnumTfRenderingMarkup](/windows/desktop/TSF/ienumtfrenderingmarkup), and [TF\_RENDERINGMARKUP](/windows/desktop/TSF/tf-renderingmarkup) described in this reference are not defined in IDL or header files. The following prototypes are needed to be complied by MIDL compiler to get the header file..


```C++
typedef struct
{
    ITfRange *pRange;
    TF_DISPLAYATTRIBUTE tfDisplayAttr;
} TF_RENDERINGMARKUP;

// 
// IEnumTfRenderingMarkup 
// 
[
  object,
  uuid(8c03d21b-95a7-4ba0-ae1b-7fce12a72930),
  pointer_default(unique)
]
interface IEnumTfRenderingMarkup : IUnknown
{
    HRESULT Clone([out] IEnumTfRenderingMarkup **ppClone);

    HRESULT Next([in] ULONG ulCount,
                 [out, size_is(ulCount), length_is(*pcFetched)] TF_RENDERINGMARKUP *rgMarkup,
                 [out] ULONG *pcFetched);

    HRESULT Reset();

    HRESULT Skip([in] ULONG ulCount);
};

// 
// ITfContextRenderingMarkup 
// 
[
  object,
  uuid(a305b1c0-c776-4523-bda0-7c5a2e0fef10),
  pointer_default(unique)
]
interface ITfContextRenderingMarkup : IUnknown
{
    const DWORD TF_GRM_INCLUDE_PROPERTY = 0x1;

    HRESULT GetRenderingMarkup([in] TfEditCookie ec,
                               [in] DWORD dwFlags,
                               [in] ITfRange *pRangeCover,
                               [out] IEnumTfRenderingMarkup **ppEnum);
                                                           
    HRESULT FindNextRenderingMarkup([in] TfEditCookie ec,
                                    [in] DWORD dwFlags,
                                    [in] ITfRange *pRangeQuery,
                                    [in] TfAnchor tfAnchorQuery,
                                    [out] ITfRange **ppRangeFound,
                                    [out] TF_RENDERINGMARKUP *ptfRenderingMarkup);
};
```



 

 