---
description: The ManageChannel method constructs an application protocol data unit (APDU) command that opens and closes logical channels.
ms.assetid: a55b5b3f-0404-45bd-afeb-e96173319a50
title: ISCardISO7816::ManageChannel method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816.ManageChannel
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816::ManageChannel method

\[The **ManageChannel** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **ManageChannel** method constructs an [*application protocol data unit*](../secgloss/a-gly.md) (APDU) command that opens and closes logical channels.

The open function opens a new logical channel other than the basic one. Options are provided for the card to assign a logical channel number, or for the logical channel number to be supplied to the card.

The close function explicitly closes a logical channel other than the basic one. After the successful closing, the logical channel shall be available for re-use.

## Syntax


```C++
HRESULT ManageChannel(
  [in]      BYTE       byChannelState,
  [in]      BYTE       byChannel,
  [in, out] LPSCARDCMD *ppCmd
);
```



## Parameters

<dl> <dt>

*byChannelState* \[in\]
</dt> <dd>

Bit b8 of P1 is used to indicate the open function or the close function; if b8 is 0, then MANAGE CHANNEL shall open a logical channel and if b8 is 1, then MANAGE CHANNEL shall close a logical channel:

P1 = '00' to open

P1 = '80' to close

Other values are RFU

</dd> <dt>

*byChannel* \[in\]
</dt> <dd>

For the open function (P1 = '00'), the bits b1 and b2 of P2 are used to code the logical channel number in the same manner as in the class byte, the other bits of P2 are RFU.

When b1 and b2 of P2 are **NULL**, then the card will assign a logical channel number that will be returned in bits b1 and b2 of the data field.

When b1 and/or b2 of P2 are not **NULL**, they code a logical channel number other than the basic one; then the card will open the externally assigned logical channel number.

</dd> <dt>

*ppCmd* \[in, out\]
</dt> <dd>

On input, a pointer to an [**ISCardCmd**](iscardcmd.md) interface object or **NULL**.

On return, it is filled with the APDU command constructed by this operation. If *ppCmd* was set to **NULL**, a [*smart card*](../secgloss/s-gly.md) [**ISCardCmd**](iscardcmd.md) object is internally created and returned using the *ppCmd* pointer.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

When the open function is successfully performed from the basic logical channel, the MF shall be implicitly selected as the current DF and the security status of the new logical channel should be the same as the basic logical channel after ATR. The security status of the new logical channel should be separate from that of any other logical channel.

When the open function is successfully performed from a logical channel, which is not the basic one, the current DF of the logical channel that issued the command will be selected as the current DF. In addition, the security status for the new logical channel should be the same as the security status of the logical channel from which the open function was performed.

After a successful close function, the security status related to this logical channel is lost.

For a list of all the methods provided by this interface, see [**ISCardISO7816**](iscardiso7816.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardssp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardsrv.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardISO7816 is defined as 53B6AA68-3F56-11D0-916B-00AA00C18068<br/>        |



## See also

<dl> <dt>

[**ISCardISO7816**](iscardiso7816.md)
</dt> </dl>

 

 
