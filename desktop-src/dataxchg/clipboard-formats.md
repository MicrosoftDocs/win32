---
title: Clipboard Formats
description: A window can place more than one object on the clipboard, each representing the same information in a different clipboard format. Users need not be aware of the clipboard formats used for an object on the clipboard.
ms.assetid: fe42baec-6b00-4816-b379-7f335da8a197
keywords:
- clipboard,formats
- clipboard,windows
- clipboard,standard formats
- clipboard,registered formats
- clipboard,synthesized formats
- standard clipboard formats
- registered clipboard formats
- synthesized clipboard formats
- cloud clipboard formats
- clipboard history formats
ms.topic: article
ms.date: 05/31/2018
---

# Clipboard Formats

A window can place more than one object on the clipboard, each representing the same information in a different clipboard format. Users need not be aware of the clipboard formats used for an object on the clipboard.

The following topics describe the clipboard formats.

-   [Standard Clipboard Formats](#standard-clipboard-formats)
-   [Registered Clipboard Formats](#registered-clipboard-formats)
-   [Private Clipboard Formats](#private-clipboard-formats)
-   [Multiple Clipboard Formats](#multiple-clipboard-formats)
-   [Synthesized Clipboard Formats](#synthesized-clipboard-formats)
-   [Cloud Clipboard and Clipboard History Formats](#cloud-clipboard-and-clipboard-history-formats)

## Standard Clipboard Formats

The clipboard formats defined by the system are called *standard clipboard formats*. These clipboard formats are described in [**Standard Clipboard Formats**](standard-clipboard-formats.md).

## Registered Clipboard Formats

Many applications work with data that cannot be translated into a standard clipboard format without loss of information. These applications can create their own clipboard formats. A clipboard format that is defined by an application, is called a [registered clipboard format](#registered-clipboard-formats). For example, if a word-processing application copied formatted text to the clipboard using a standard text format, the formatting information would be lost. The solution would be to register a new clipboard format, such as Rich Text Format (RTF).

To register a new clipboard format, use the [**RegisterClipboardFormat**](/windows/desktop/api/Winuser/nf-winuser-registerclipboardformata) function. This function takes the name of the format and returns an unsigned integer value that represents the registered clipboard format. To retrieve the name of the registered clipboard format, pass the unsigned integer value to the [**GetClipboardFormatName**](/windows/desktop/api/Winuser/nf-winuser-getclipboardformatnamea) function.

If more than one application registers a clipboard format with exactly the same name, the clipboard format is registered only once. Both calls to the [**RegisterClipboardFormat**](/windows/desktop/api/Winuser/nf-winuser-registerclipboardformata) function return the same value. In this way, two different applications can share data by using a registered clipboard format.

## Private Clipboard Formats

An application can identify a private clipboard format by defining a value in the range **CF\_PRIVATEFIRST** through **CF\_PRIVATELAST**. An application can use a private clipboard format for an application-defined data format that does not need to be registered with the system.

Data handles associated with private clipboard formats are not automatically freed by the system. If your windows use private clipboard formats, you can use the [**WM\_DESTROYCLIPBOARD**](wm-destroyclipboard.md) message to free any related resources that are no longer needed.

For more information about the [**WM\_DESTROYCLIPBOARD**](wm-destroyclipboard.md) message, see [Clipboard Ownership](clipboard-operations.md).

An application can place data handles on the clipboard by defining a private format in the range **CF\_GDIOBJFIRST** through **CF\_GDIOBJLAST**. When using values in this range, the data handle is not a handle to a Windows Graphics Device Interface (GDI) object, but is a handle allocated by the [**GlobalAlloc**](/windows/desktop/api/winbase/nf-winbase-globalalloc) function with the GMEM\_MOVEABLE flag. When the clipboard is emptied the system automatically deletes the object using the [**GlobalFree**](/windows/desktop/api/winbase/nf-winbase-globalfree) function.

## Multiple Clipboard Formats

A window can place more than one clipboard object on the clipboard, each representing the same information in a different clipboard format. When placing information on the clipboard, the window should provide data in as many formats as possible. To find out how many formats are currently used on the clipboard, call the [**CountClipboardFormats**](/windows/desktop/api/Winuser/nf-winuser-countclipboardformats) function.

Clipboard formats that contain the most information should be placed on the clipboard first, followed by less descriptive formats. A window pasting information from the clipboard typically retrieves a clipboard object in the first format it recognizes. Because clipboard formats are enumerated in the order they are placed on the clipboard, the first recognized format is also the most descriptive.

For example, suppose a user copies styled text from a word-processing document. The window containing the document might first place data on the clipboard in a registered format, such as RTF. Subsequently, the window would place data on the clipboard in a less descriptive format, such as text (**CF\_TEXT**).

When the content of the clipboard is pasted into another window, the window retrieves data in the most descriptive format it recognizes. If the window recognizes RTF, the corresponding data is pasted into the document. Otherwise, the text data is pasted into the document and the formatting information is lost.

## Synthesized Clipboard Formats

The system implicitly converts data between certain clipboard formats: if a window requests data in a format that is not on the clipboard, the system converts an available format to the requested format. The system can convert data as indicated in the following table.



| Clipboard Format     | Conversion Format    |
|----------------------|----------------------|
| **CF\_BITMAP**       | **CF\_DIB**          |
| **CF\_BITMAP**       | **CF\_DIBV5**        |
| **CF\_DIB**          | **CF\_BITMAP**       |
| **CF\_DIB**          | **CF\_PALETTE**      |
| **CF\_DIB**          | **CF\_DIBV5**        |
| **CF\_DIBV5**        | **CF\_BITMAP**       |
| **CF\_DIBV5**        | **CF\_DIB**          |
| **CF\_DIBV5**        | **CF\_PALETTE**      |
| **CF\_ENHMETAFILE**  | **CF\_METAFILEPICT** |
| **CF\_METAFILEPICT** | **CF\_ENHMETAFILE**  |
| **CF\_OEMTEXT**      | **CF\_TEXT**         |
| **CF\_OEMTEXT**      | **CF\_UNICODETEXT**  |
| **CF\_TEXT**         | **CF\_OEMTEXT**      |
| **CF\_TEXT**         | **CF\_UNICODETEXT**  |
| **CF\_UNICODETEXT**  | **CF\_OEMTEXT**      |
| **CF\_UNICODETEXT**  | **CF\_TEXT**         |



 

If the system provides an automatic type conversion for a particular clipboard format, there is no advantage to placing the conversion format(s) on the clipboard.

If the system provides an automatic type conversion for a particular clipboard format, and you call [**EnumClipboardFormats**](/windows/desktop/api/Winuser/nf-winuser-enumclipboardformats) to enumerate the clipboard data formats, the system first enumerates the format that is on the clipboard, followed by the formats to which it can be converted.

When copying bitmaps, it is best to place the **CF\_DIB** or **CF\_DIBV5** format on the clipboard. This is because the colors in a device-dependent bitmap (**CF\_BITMAP**) are relative to the system palette, which may change before the bitmap is pasted. If the **CF\_DIB** or **CF\_DIBV5** format is on the clipboard and a window requests the **CF\_BITMAP** format, the system renders the device-independent bitmap (DIB) using the current palette at that time.

If you place the **CF\_BITMAP** format on the clipboard (and not **CF\_DIB**), the system renders the **CF\_DIB** or **CF\_DIBV5** clipboard format as soon as the clipboard is closed. This ensures that the correct palette is used to generate the DIB. If you place the **CF\_DIBV5** format with the bitmap color space information in the clipboard, the system will convert the bitmap bits from the bitmap color space to the sRGB color space when **CF\_DIB** or **CF\_DIBV5** is requested. If **CF\_DIBV5** is requested when there is no color space information in the clipboard, the system returns sRGB color space information in the [**BITMAPV5HEADER**](/windows/desktop/api/wingdi/ns-wingdi-bitmapv5header) structure. Conversions between other clipboard formats occur upon demand.

If the clipboard contains data in the **CF\_PALETTE** format, the application should use the [**SelectPalette**](/windows/desktop/api/wingdi/nf-wingdi-selectpalette) and [**RealizePalette**](/windows/desktop/api/wingdi/nf-wingdi-realizepalette) functions to realize any other data in the clipboard against that logical palette.

There are two clipboard formats for metafiles: **CF\_ENHMETAFILE** and **CF\_METAFILEPICT**. Specify **CF\_ENHMETAFILE** for enhanced metafiles and **CF\_METAFILEPICT** for Windows metafiles.

## Cloud Clipboard and Clipboard History Formats

Some versions of Windows include [Cloud Clipboard](/windows/whats-new/whats-new-windows-10-version-1809#cloud-clipboard),
which keeps a history of recent clipboard data items and can synchronize it between the user's devices.
If you don't want the data your application places on the clipboard to be included
in the clipboard history or synchronized with other devices, your application can control
this behavior by placing data in certain [registered clipboard formats](#registered-clipboard-formats)
whose names are known to the Windows system:

- **ExcludeClipboardContentFromMonitorProcessing** : Place any data on the clipboard in this format
  to prevent all clipboard formats being included in the clipboard history or synchronized to the
  user's other devices.
- **CanIncludeInClipboardHistory** : Place a serialized **[DWORD](../WinProg/windows-data-types.md)**
  value of zero on the clipboard in this format to prevent all clipboard formats being included
  in the clipboard history, or place a value of one instead to explicitly request that
  the clipboard item be included in the clipboard history. This does not affect synchronization
  to the user's other devices.
- **CanUploadToCloudClipboard** : Place a serialized **[DWORD](../WinProg/windows-data-types.md)**
  value of zero on the clipboard in this format to prevent all clipboard formats being synchronized
  to the user's other devices, or place a value of one instead to explicitly request that
  the clipboard item be synchronized to other devices. This does not affect the local device's
  clipboard history.

As with other registered clipboard formats, you will need to use the [**RegisterClipboardFormat**](
/windows/win32/api/winuser/nf-winuser-registerclipboardformata) function to obtain an unsigned
integer value that identifies each of the above 3 formats.