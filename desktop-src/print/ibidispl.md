---
Description: The IBidiSpl interface allows an application or other objects to send a single bidi request or a list of bidi requests.
ms.assetid: 7e4a30b2-ac3a-475a-b818-455cdb7a91bf
title: IBidiSpl interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IBidiSpl interface

The **IBidiSpl** interface allows an application or other objects to send a single bidi request or a list of bidi requests.

## Members

The **IBidiSpl** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IBidiSpl** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBidiSpl** interface has these methods.



| Method                                                    | Description                                   |
|:----------------------------------------------------------|:----------------------------------------------|
| [**BindDevice**](ibidispl-ibidispl--binddevice.md)       | Binds a printer to a bidi request.<br/> |
| [**MultiSendRecv**](ibidispl-ibidispl--multisendrecv.md) | Sends a list of bidi requests.<br/>     |
| [**SendRecv**](ibidispl-ibidispl--sendrecv.md)           | Sends a bidi request.<br/>              |
| [**UnbindDevice**](ibidispl-ibidispl--unbinddevice.md)   | Unbinds a printer.<br/>                 |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Bidispl.h</dt> </dl> |



## See also

<dl> <dt>

[Bidirectional Communication Interfaces](bidirectional-communication-interfaces.md)
</dt> <dt>

[Bidirectional Communication Schema](https://www.bing.com/search?q=Bidirectional+Communication+Schema)
</dt> <dt>

[**IBidiSpl**](ibidirequestcontainer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiSpl%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





