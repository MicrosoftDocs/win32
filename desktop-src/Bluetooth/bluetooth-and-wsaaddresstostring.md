---
title: Bluetooth and WSAAddressToString
description: The WSAAddressToString Windows Sockets function is used to convert a Bluetooth Device Address to a string, which is in turn provided to the WSALookupServiceBegin function via the WSAQUERYSET structure when retrieving device service information.
ms.assetid: 3489d29a-2b64-4051-b579-57878efc0c73
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and WSAAddressToString

The [**WSAAddressToString**](https://msdn.microsoft.com/library/windows/desktop/ms741516) Windows Sockets function is used to convert a Bluetooth Device Address to a string, which is in turn provided to the [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633) function via the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure when retrieving device service information.

While a Bluetooth Device Address fits within a 20 character buffer, the [**WSAAddressToString**](https://msdn.microsoft.com/library/windows/desktop/ms741516) function currently returns **WSAEFAULT** for Bluetooth Device Addresses unless the buffer and the specified *lpdwAddressStringLength* value are set to a character length of 40.

> [!Note]  
> When **WSAEFAULT** is returned by [**WSAAddressToString**](https://msdn.microsoft.com/library/windows/desktop/ms741516) as the result of an insufficient buffer, the *lpdwAddressStringLength* parameter is not updated with the buffer size required for the operation.

 

## Related topics

<dl> <dt>

[**WSAAddressToString**](https://msdn.microsoft.com/library/windows/desktop/ms741516)
</dt> <dt>

[Bluetooth and WSALookupServiceBegin](bluetooth-and-wsalookupservicebegin.md)
</dt> <dt>

[Bluetooth and WSAQUERYSET](bluetooth-and-wsaqueryset.md)
</dt> </dl>

 

 




