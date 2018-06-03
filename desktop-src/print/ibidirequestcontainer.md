---
Description: The IBidiRequestContainer interface allows an application or other objects to compose and retrieve a list of bidi requests.
ms.assetid: 21dfcbe8-2fc1-4495-af54-5d4c83b8bb79
title: IBidiRequestContainer interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IBidiRequestContainer interface

The **IBidiRequestContainer** interface allows an application or other objects to compose and retrieve a list of bidi requests.

## Members

The **IBidiRequestContainer** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IBidiRequestContainer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBidiRequestContainer** interface has these methods.



| Method                                                                                  | Description                                               |
|:----------------------------------------------------------------------------------------|:----------------------------------------------------------|
| [**AddRequest**](ibidirequestcontainer-ibidirequestcontainer--addrequest.md)           | Adds a request to the request list.<br/>            |
| [**GetEnumObject**](ibidirequestcontainer-ibidirequestcontainer--getenumobject.md)     | Enumerates the number of requests in the list.<br/> |
| [**GetRequestCount**](ibidirequestcontainer-ibidirequestcontainer--getrequestcount.md) | Gets the number of requests in the list.<br/>       |



 

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

[Bidirectional Communication Schema](https://www.bing.com/search?q=Bidirectional Communication Schema)
</dt> <dt>

[Print Spooler Components](https://www.bing.com/search?q=Print Spooler Components)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequestContainer%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





