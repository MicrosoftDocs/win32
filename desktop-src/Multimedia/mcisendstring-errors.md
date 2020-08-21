---
title: mciSendString Errors
description: mciSendString Errors
ms.assetid: 286102bd-fcf3-425b-9adc-e0ca2d62e453
keywords:
- MCIERR return values,mciSendString errors
- multimedia reference,mciSendString errors
- reference for multimedia,mciSendString errors
- Media Control Interface (MCI),mciSendString errors
- MCI (Media Control Interface),mciSendString errors
- reference for MCI,mciSendString errors
- MCI reference,mciSendString errors
- Media Control Interface (MCI),errors
- MCI (Media Control Interface),errors
- reference for MCI,errors
- MCI reference,errors
- mciSendString errors
- mciSendString function
ms.topic: article
ms.date: 05/31/2018
---

# mciSendString Errors

The following errors are returned by the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function but not by [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)):



| Value                             | Meaning                                           |
|-----------------------------------|---------------------------------------------------|
| MCIERR\_BAD\_CONSTANT             | The value specified for a parameter is unknown.   |
| MCIERR\_BAD\_INTEGER              | An integer in the command was invalid or missing. |
| MCIERR\_DUPLICATE\_FLAGS          | A flag or value was specified twice.              |
| MCIERR\_MISSING\_COMMAND\_STRING  | No command was specified.                         |
| MCIERR\_MISSING\_DEVICE\_NAME     | No device name was specified.                     |
| MCIERR\_MISSING\_STRING\_ARGUMENT | A string value was missing from the command.      |
| MCIERR\_NEW\_REQUIRES\_ALIAS      | An alias must be used with the "new" device name. |
| MCIERR\_NO\_CLOSING\_QUOTE        | A closing quotation mark is missing.              |
| MCIERR\_NOTIFY\_ON\_AUTO\_OPEN    | The "notify" flag is illegal with auto-open.      |
| MCIERR\_PARAM\_OVERFLOW           | The output string was not long enough.            |
| MCIERR\_PARSER\_INTERNAL          | An internal parser error occurred.                |
| MCIERR\_UNRECOGNIZED\_KEYWORD     | An unknown command parameter was specified.       |



 

 

 