---
description: Represents a tablet attached to the computer.
ms.assetid: 31e11f7d-5610-4c49-9203-2dc322fbef95
title: ITablet interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet interface

Represents a tablet attached to the computer.

## Members

The **ITablet** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITablet** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITablet** interface has these methods.



| Method                                                                 | Description                                                                           |
|:-----------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**CreateContext**](itablet-createcontext.md)                         | Creates a context object that describes the specified tablet device.<br/>       |
| [**GetCursor**](/previous-versions/windows/desktop/legacy/aa373535(v=vs.85))                                 | Retrieves the specified [**ITabletCursor**](itabletcursor.md) object.<br/>     |
| [**GetCursorCount**](itablet-getcursorcount.md)                       | Retrieves the number of cursor objects associated with the tablet.<br/>         |
| [**GetDefaultContextSettings**](itablet-getdefaultcontextsettings.md) | Retrieves the default context settings for the tablet.<br/>                     |
| [**GetHardwareCaps**](itablet-gethardwarecaps.md)                     | Retrieves a value that represents the capabilities of the tablet hardware.<br/> |
| [**GetMaxInputRect**](itablet-getmaxinputrect.md)                     | Retrieves a rectangle that represents maximum input area of the tablet.<br/>    |
| [**GetName**](itablet-getname.md)                                     | Retrieves a string containing the name of the tablet device.<br/>               |
| [**GetPlugAndPlayId**](itablet-getplugandplayid.md)                   | Retrieves a string containing the Plug and Play ID for the tablet device.<br/>  |
| [**GetPropertyMetrics**](/previous-versions/windows/desktop/legacy/aa367722(v=vs.85))               | Retrieves the metrics data for a specified property.<br/>                       |



 

## Remarks

Developers should not use this interface.

The following code describes how the **ITablet** interface is defined.

``` syntax
[
    object,
   uuid(1CB2EFC3-ABC7-4172-8FCB-3BC9CB93E29F),
    pointer_default(unique)
]
interface ITablet : IUnknown
{
    HRESULT GetDefaultContextSettings(
        [out] TABLET_CONTEXT_SETTINGS **ppTCS);

    HRESULT CreateContext(
        [in] HWND hWnd,
        [in, unique] RECT *prcInput,
        [in] DWORD dwOptions,
        [in, unique] TABLET_CONTEXT_SETTINGS *pTCS,
        [in] CONTEXT_ENABLE_TYPE cet,
        [out] ITabletContext **ppCtx,
        [in, out, unique] TABLET_CONTEXT_ID *pTcid,
        [in, out, unique] PACKET_DESCRIPTION **ppPD,
        [in, unique] ITabletEventSink *pSink);

    HRESULT GetName(
        [out] LPWSTR *ppwszName);

    HRESULT GetMaxInputRect(
        [out] RECT *prcInput);

    HRESULT GetHardwareCaps(
        [out] DWORD *pdwCaps);

    HRESULT GetPropertyMetrics(
        [in] REFGUID rguid,
        [out] PROPERTY_METRICS *pPM);

    HRESULT GetPlugAndPlayId(
        [out] LPWSTR *ppwszPPId);

    HRESULT GetCursorCount(
        [out] ULONG *pcCurs);

    HRESULT GetCursor(
        [in] ULONG iCur,
        [out] ITabletCursor **ppCur);
};   
```

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



 

