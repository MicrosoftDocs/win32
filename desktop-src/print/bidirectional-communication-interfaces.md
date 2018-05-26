---
Description: Bidirectional Communication Interfaces
ms.assetid: 5dbc3e61-3346-4e89-96c8-b214719177f0
title: Bidirectional Communication Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bidirectional Communication Interfaces

The following interfaces are used in bidi communication.



| Interface                                                     | Description                                                |
|---------------------------------------------------------------|------------------------------------------------------------|
| [IBidiRequest](ibidirequest.md)<br/>                   | Compose a bidi request.<br/>                         |
| [IBidiRequestContainer](ibidirequestcontainer.md)<br/> | Compose and retrieve a list of bidi requests.<br/>   |
| [IBidiSpl](ibidispl.md)<br/>                           | Send a bidi request or a list of bidi requests.<br/> |
| [IBidiSpl2](ibidispl2.md)<br/>                         | Send bidi requests as XML strings or streams.<br/>   |



 

The [IBidiSpl2](ibidispl2.md) interface, which is introduced in Windows Vista, enables an application or driver to send bidi requests by using XML rather than function calls. This XML exchange uses the bidi communication request and response schema, and the XML objects can be either strings or IStreams.

For more information about the bidirectional communication interfaces, see the [Printing and Print Spooler Interfaces](http://go.microsoft.com/fwlink/p/?linkid=70002) section in the Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Bidirectional%20Communication%20Interfaces%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




