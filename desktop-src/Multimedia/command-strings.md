---
title: Command Strings
description: Command Strings
ms.assetid: ca9ca153-f2bf-45ed-84e6-44e86e8efaed
keywords:
- MCI command strings,about
- MCI command strings,syntax
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Command Strings

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To send a string command to an MCI device, use the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function, which includes parameters for the string command and a buffer for any returned information.

The **mciSendString** function returns zero if successful. If the function fails, the low-order word of the return value contains an error code. You can pass this error code to the [**mciGetErrorString**](/previous-versions//dd757158(v=vs.85)) function to get a text description of the error.

## Syntax of Command Strings

MCI command strings use a consistent verb-object-modifier syntax. Each command string includes a command, a device identifier, and command arguments. Arguments are optional for some commands and required for others.

A command string has the following form:

*command device\_id arguments*

These components contain the following information:

-   The *command* specifies an MCI command, such as [**open**](open.md), [**close**](close.md), or [**play**](play.md).
-   The *device\_id* identifies an instance of an MCI driver. The *device\_id* is created when the device is opened.
-   The *arguments* specify the flags and variables used by the command. Flags are keywords recognized with the MCI command. Variables are numbers or strings that apply to the MCI command or flag.

    For example, the **play** command uses the arguments "from *position* " and "to *position* " to indicate the positions at which to start and end play. You can list the flags used with a command in any order. When you use a flag that has a variable associated with it, you must supply a value for the variable.

    Unspecified (and optional) command arguments assume a default value.

The following example function sends the [**play**](play.md) command with the "from" and "to" flags.


```C++
BOOL PlayFromTo(LPTSTR lpstrAlias, DWORD dwFrom, DWORD dwTo) 
{ 
    TCHAR achCommandBuff[128]; 
    int result;
    MCIERROR err;

    // Form the command string.
    result = _stprintf_s(
        achCommandBuff, 
        TEXT("play %s from %u to %u"), 
        lpstrAlias, dwFrom, dwTo); 

    if (result == -1)
    {
        return FALSE;
    }

    // Send the command string.
    err = mciSendString(achCommandBuff, NULL, 0, NULL); 
    if (err != 0)
    {
        return FALSE;
    }

    return TRUE;
} 
```



## Data Types for Command Variables

You can use the following data types for the variables in a command string.



| **Data type**        | **Description**                                                                                                                                                                                                                                                                                                                                                |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Strings              | String data types are delimited by leading and trailing white spaces and quotation marks. MCI removes single quotation marks from a string. To put a quotation mark in a string, use a set of two quotation marks where you want to embed your quotation mark. To use an empty string, use two quotation marks delimited by leading and trailing white spaces. |
| Signed long integers | Signed long integer data types are delimited by leading and trailing white spaces. Unless otherwise specified, integers can be positive or negative. If you use negative integers, you should not separate the minus sign and the first digit with a space.                                                                                                    |
| Rectangles           | Rectangle data types are an ordered list of four signed short values. White space delimits this data type and separates each integer in the list.                                                                                                                                                                                                              |



 

 

 