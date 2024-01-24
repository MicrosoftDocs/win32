---
description: Creates a context object that describes the specified tablet device.
ms.assetid: 76f48485-a958-4457-9b87-73de73fa671e
title: ITablet::CreateContext method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITablet.CreateContext
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITablet::CreateContext method

Creates a context object that describes the specified tablet device.

## Syntax


```C++
HRESULT CreateContext(
  [in]      HWND                    hWnd,
  [in]      RECT                    *prcInput,
  [in]      DWORD                   dwOptions,
  [in]      TABLET_CONTEXT_SETTINGS *pTCS,
  [in]      CONTEXT_ENABLE_TYPE     cet,
  [out]     ITabletContext          **ppCtx,
  [in, out] TABLET_CONTEXT_ID       *pTcid,
  [in, out] PACKET_DESCRIPTION      **ppPD,
  [in]      ITabletEventSink        *pSink
);
```



## Parameters

<dl> <dt>

*hWnd* \[in\]
</dt> <dd>

The window to which the tablet context will be attached.

</dd> <dt>

*prcInput* \[in\]
</dt> <dd>

\[in, unique\]

The ink input rectangle.

</dd> <dt>

*dwOptions* \[in\]
</dt> <dd>

Flags that set tablet context options.

</dd> <dt>

*pTCS* \[in\]
</dt> <dd>

\[in, unique\]

Detailed information about the tablet context to create.

</dd> <dt>

*cet* \[in\]
</dt> <dd>

Value that enables or disables context messages being sent to the window.

</dd> <dt>

*ppCtx* \[out\]
</dt> <dd>

A pointer to the newly create tablet context.

</dd> <dt>

*pTcid* \[in, out\]
</dt> <dd>

Value that uniquely identifies the tablet.

</dd> <dt>

*ppPD* \[in, out\]
</dt> <dd>

Pointer to information about what data is contained in each packet.

</dd> <dt>

*pSink* \[in\]
</dt> <dd>

The [**ITabletEventSink**](itableteventsink.md) object where notification messages will be sent.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

Typically, an application obtains the default values from the [**ITablet::GetDefaultContextSettings Method**](itablet-getdefaultcontextsettings.md), modifies values to suit their needs, and then passes the modified settings structure to the **ITablet::CreateContext Method**.

> [!Note]  
> You must implement the [**ITabletEventSink Interface**](itableteventsink.md) when calling the **ITablet::CreateContext Method**.

 

The *dwOptions* parameter is a set of bit flags that describe context options. The following table describes these flags.



| Flag Name                                | Value                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                              |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TCXO\_MARGIN<br/>                  | 0x00000001<br/>                                                                                                                                                                         | Specifies that the input context on the tablet will have a margin. The margin is an area outside the specified input area where events will be mapped to the edge of the input area. This feature makes it easier to input points at the edge of the context.<br/> |
| TCXO\_PREHOOK<br/>                 | 0x00000002<br/>                                                                                                                                                                         | Prehook gets packets before regular contexts and posthooks. They get packets in the order of their creation.<br/>                                                                                                                                                  |
| TCXO\_CURSOR\_STATE<br/>           | 0x00000004<br/>                                                                                                                                                                         | The TC will return packets even if the cursor is up. By default, a TC will only return packets when the cursor is down.<br/>                                                                                                                                       |
| TCXO\_NO\_CURSOR\_DOWN<br/>        | 0x00000008<br/>                                                                                                                                                                         | The TC will not return packets when the cursor is down.<br/>                                                                                                                                                                                                       |
| TCXO\_NON\_INTEGRATED<br/>         | 0x00000010<br/>                                                                                                                                                                         | The context will be non-integrated.<br/>                                                                                                                                                                                                                           |
| TCXO\_POSTHOOK<br/>                | 0x00000020<br/>                                                                                                                                                                         | Posthooks get packets after regular tablet contexts but before the system context. They get packets in the reverse order of their creation.<br/>                                                                                                                   |
| TCXO\_DONT\_SHOW\_CURSOR<br/>      | 0x00000080<br/>                                                                                                                                                                         | The TC will not set the cursor position.<br/>                                                                                                                                                                                                                      |
| TCXO\_DONT\_VALIDATE\_TCS<br/>     | 0x00000100<br/>                                                                                                                                                                         | The TC will not validate the GUIDS passed in the tablet context settings against the supported properties of the device.<br/>                                                                                                                                      |
| TCXO\_ALLOW\_FLICKS<br/>           | 0x00000400<br/>                                                                                                                                                                         | The TC will allow flick detection to take place (by default this is only allowed on system contexts), and the client will get SE\_FLICK events.<br/>                                                                                                               |
| TCXO\_ALLOW\_FEEDBACK\_TAPS<br/>   | 0x00000800<br/>                                                                                                                                                                         | The TC will allow pen feedback to be shown. By default, this is only allowed on system contexts.<br/>                                                                                                                                                              |
| TCXO\_ALLOW\_FEEDBACK\_BARREL<br/> | 0x00001000<br/>                                                                                                                                                                         | The TC will allow pen feedback to be shown. By default, this is only allowed on system contexts.<br/>                                                                                                                                                              |
| TCXO\_ALL<br/>                     | TCXO\_MARGIN \| TCXO\_PREHOOK \| TCXO\_CURSOR\_STATE \| TCXO\_NO\_CURSOR\_DOWN \| TCXO\_NON\_INTEGRATED \| TCXO\_POSTHOOK \| TCXO\_DONT\_SHOW\_CURSOR \| TCXO\_DONT\_VALIDATE\_TCS<br/> | All defined tablet context options.<br/>                                                                                                                                                                                                                           |
| TCXO\_HOOK<br/>                    | TCXO\_PREHOOK \| TCXO\_POSTHOOK<br/>                                                                                                                                                    | Combines pre-hook and post-hook functionality.<br/>                                                                                                                                                                                                                |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITablet Interface**](itablet.md)
</dt> <dt>

[**CONTEXT\_ENABLE\_TYPE Enumeration**](context-enable-type.md)
</dt> <dt>

[**TABLET\_CONTEXT\_SETTINGS Structure**](tablet-context-settings.md)
</dt> <dt>

[**PACKET\_DESCRIPTION Structure**](/windows/desktop/api/tpcshrd/ns-tpcshrd-packet_description)
</dt> <dt>

[**ITabletContextP Interface**](itabletcontextp.md)
</dt> <dt>

[**ITabletEventSink Interface**](itableteventsink.md)
</dt> </dl>

 

 




