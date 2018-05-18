---
Description: 'Retrieves an ATR string of the smart card.'
ms.assetid: '2021bd0c-6ef8-4679-be6c-9a9fd33d9fd6'
title: 'ISCard::get\_Atr method'
---

# ISCard::get\_Atr method

\[The **get\_Atr** method is available for use in the operating systems specified in the Requirements section. The [Smart Card Modules](secsmart.smart_card_modules) provide similar functionality.\]

The **get\_Atr** method retrieves an [*ATR string*](security.a_gly#-security-atr-string-gly) of the [*smart card*](security.s_gly#-security-smart-card-gly).

## Syntax


```C++
HRESULT get_Atr(
  [out] LPBYTEBUFFER *ppAtr
);
```



## Parameters

<dl> <dt>

*ppAtr* \[out\]
</dt> <dd>

Pointer to a byte buffer in the form of an [**IStream**](stg.istream) that will contain the ATR string on return.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *ppAtr* parameter is not valid.<br/>           |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *ppAtr*.<br/>          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Memory to satisfy the request is unavailable.<br/> |



 

## Remarks

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md#smart-card-return-values).

## Examples

The following example shows retrieving the ATR string from the smart card.


```C++
// Retrieve the ATR.
// pISCard is a pointer to a previously instantiated ISCard.
// pAtr is a pointer to a previously instantiated IByteBuffer.
hr = pISCard->get_Atr(&amp;pAtr);
if (FAILED(hr))
{
    printf("Failed get_Atr\n");
    // Take other error handling action.
}
// Success, you can now use IByteBuffer::Read to access ATR bytes.
BYTE  byAtr[32];
   long  lBytesRead, i;
   // Read the ATR string into a byte array.
   hr = pAtr->Read(byAtr, 32, &amp;lBytesRead);
   // Use the ATR value. (This example merely displays the bytes.)
   for ( i = 0; i < lBytesRead; i++)
       printf("%c", *(byAtr + i));
   printf("\n");
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardmgr.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardmgr.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCard is defined as 1461AAC3-6810-11D0-918F-00AA00C18068<br/>               |



## See also

<dl> <dt>

[**get\_CardHandle**](iscard-get-cardhandle.md)
</dt> <dt>

[**get\_Context**](iscard-get-context.md)
</dt> <dt>

[**get\_Protocol**](iscard-get-protocol.md)
</dt> <dt>

[**get\_Status**](iscard-get-status.md)
</dt> <dt>

[**ISCard**](iscard.md)
</dt> <dt>

[**IByteBuffer::Read**](ibytebuffer-read.md)
</dt> </dl>

 

 




