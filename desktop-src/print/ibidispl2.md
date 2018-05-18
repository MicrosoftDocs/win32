---
Description: 'The IBidiSpl2 interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas.'
ms.assetid: '90e8a390-7d30-4bcf-8c81-438c86529ceb'
title: IBidiSpl2 interface
---

# IBidiSpl2 interface

The **IBidiSpl2** interface enables an application or other objects to send one or more bidi requests using one of the Bidi Request Schemas and receive information formatted as one of the Bidi Response Schemas. The requests and responses can be either strings or Streams.

## Members

The **IBidiSpl2** interface inherits from the [**IUnknown**](com.iunknown) interface. **IBidiSpl2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBidiSpl2** interface has these methods.



| Method                                                              | Description                                                                                                                                           |
|:--------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BindDevice**](ibidispl2-ibidispl2--binddevice.md)               | Binds a printer to a bidirectional communication request.<br/>                                                                                  |
| [**SendRecvXMLStream**](ibidispl2-ibidispl2--sendrecvxmlstream.md) | Sends a bidirectional communication request (and receives the response) as Bidi Request and Response-compliant [**IStream**](stg.istream).<br/> |
| [**SendRecvXMLString**](ibidispl2-ibidispl2--sendrecvxmlstring.md) | Sends a bidirectional communication request (and receives the response) as Bidi Request and Response-compliant strings.<br/>                    |
| [**UnbindDevice**](ibidispl2-ibidispl2--unbinddevice.md)           | Releases a printer from a bidirectional communication request.<br/>                                                                             |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Bidispl.h</dt> </dl> |



## See also

<dl> <dt>

[Bidirectional Communication Interfaces](bidirectional-communication-interfaces.md)
</dt> <dt>

[Bidirectional Communication Schema](print.bidirectional_communication_schema)
</dt> <dt>

[Print Spooler Components](print.print_spooler_components)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiSpl2%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





