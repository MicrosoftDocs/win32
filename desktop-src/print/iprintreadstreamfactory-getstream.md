---
Description: The GetStream method gets the stream interface.
ms.assetid: 47447f00-a57d-4821-b10e-1b2cf7eaad94
title: IPrintReadStreamFactoryGetStream method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintReadStreamFactory::GetStream method

The `GetStream` method gets the stream interface.

## Syntax


```C++
HRESULT GetStream(
  [out] IPrintReadStream **ppStream
);
```



## Parameters

<dl> <dt>

*ppStream* \[out\]
</dt> <dd>

A pointer to an [IPrintReadStream](iprintreadstream.md) interface. The filter can use this interface to read the contents of the print ticket.

</dd> </dl>

## Return value

`GetStream` returns an **HRESULT** value.

## Remarks

The following code example shows how a filter can use **IPrintReadStreamFactory** to access the per-user print ticket.


```
VARIANT var;
VariantInit(&amp;var);

HRESULT hr = pIPropertyBag->GetProperty(
  XPS_FP_USER_PRINT_TICKET,
  &amp;var);

if (SUCCEEDED(hr))
{
 IPrintReadStreamFactory   *pPrintReadStreamFactory;

 hr = V_UNKNOWN(&amp;var)->QueryInterface(
 IID_IPrintReadStreamFactory,
 reinterpret_cast<void **>(&amp;pPrintReadStreamFactory));

 if (SUCCEEDED(hr))
    {
 IPrintReadStream *pPrintTicketStream;

 hr = pPrintReadStreamFactory->GetStream(&amp;pPrintTicketStream);

 if (SUCCEEDED(hr))
      {

       // Use the print ticket here. 
       // It's OK to cache the pointer 
       // to use now and release later.

 pPrintTicketStream->Release();
      }

 pPrintReadStreamFactory->Release();
    }

 VariantClear(&amp;var);
}
```



## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl>   |
| IDL<br/>             | <dl> <dt>Filterpipeline.idl</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintReadStreamFactory::GetStream%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




