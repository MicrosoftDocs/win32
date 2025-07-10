---
description: The HRESULT values in this article are the most common. More values are contained in the header file Winerror.h.
ms.assetid: ce52efc3-92c7-40e4-ac49-0c54049e169f
title: Common HRESULT Values
ms.topic: concept-article
ms.date: 07/09/2025
# customer intent: As a Windows developer, I want to understand the common HRESULT values so that I can handle errors effectively in my applications.
---

# Common HRESULT values

HRESULT values are used in Windows programming to indicate the success or failure of operations. They are 32-bit values that can be used to represent both success and error conditions.

## Listing of common HRESULT values

The following **HRESULT** values are the most common. More values are contained in the header file `Winerror.h`.

Here are the values listed alphabetically by name:

| Name            | Description                         | Value      |
|-----------------|-------------------------------------|------------|
| S\_OK           | Operation successful                | 0x00000000 |
| E\_ABORT        | Operation aborted                   | 0x80004004 |
| E\_ACCESSDENIED | General access denied error         | 0x80070005 |
| E\_FAIL         | Unspecified failure                 | 0x80004005 |
| E\_HANDLE       | Handle that is not valid            | 0x80070006 |
| E\_INVALIDARG   | One or more arguments are not valid | 0x80070057 |
| E\_NOINTERFACE  | No such interface supported         | 0x80004002 |
| E\_NOTIMPL      | Not implemented                     | 0x80004001 |
| E\_OUTOFMEMORY  | Failed to allocate necessary memory | 0x8007000E |
| E\_POINTER      | Pointer that is not valid           | 0x80004003 |
| E\_UNEXPECTED   | Unexpected failure                  | 0x8000FFFF |

Here are the values listed in numeric order by value:

| Value      | Name            | Description                         |
|------------|-----------------|-------------------------------------|
| 0x00000000 | S\_OK           | Operation successful                |
| 0x80004001 | E\_NOTIMPL      | Not implemented                     |
| 0x80004002 | E\_NOINTERFACE  | No such interface supported         |
| 0x80004003 | E\_POINTER      | Pointer that is not valid           |
| 0x80004004 | E\_ABORT        | Operation aborted                   |
| 0x80004005 | E\_FAIL         | Unspecified failure                 |
| 0x8000FFFF | E\_UNEXPECTED   | Unexpected failure                  |
| 0x80070005 | E\_ACCESSDENIED | General access denied error         |
| 0x80070006 | E\_HANDLE       | Handle that is not valid            |
| 0x8007000E | E\_OUTOFMEMORY  | Failed to allocate necessary memory |
| 0x80070057 | E\_INVALIDARG   | One or more arguments are not valid |

## Related content

[GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror)