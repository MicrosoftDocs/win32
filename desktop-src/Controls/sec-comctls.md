---
title: Security Considerations Microsoft Windows Controls
description: This topic provides information about security considerations related to the Windows controls.
ms.assetid: 'd5396fa1-452e-40e1-beaf-ae04690048f1'
---

# Security Considerations: Microsoft Windows Controls

This topic provides information about security considerations related to the Windows controls. The information in this topic does not provide all you need to know about security issues—use it as a starting point and reference for this technology area.

Interconnectivity among computers is common; a developer's chief concern must be application security. The following sections discuss some potential security issues to consider when programming Windows controls.

-   [Null-terminated Control Messages](#null-terminated-control-messages)
-   [String Use](#string-use)
-   [Input Validation](#input-validation)
-   [Password Use](#password-use)
-   [Security Alerts](#security-alerts)
-   [Related topics](#related-topics)

## Null-terminated Control Messages

Many of the control messages and macros have string parameters. Often these messages do not validate the input strings, in particular, they do not check for a terminating `'\0'`. When you call a message that uses a string as a parameter, explicitly specify that the string is null-terminated.

## String Use

When you program Windows controls, it is necessary to manipulate strings. Almost every control requires text to be inserted. For example, to populate a list box you must load strings into the control. Because using strings incorrectly often causes buffer overruns, take precautions to avoid this security risk.

For more information about buffer overruns, see *Writing Secure Code* by Michael Howard and David LeBlanc, Microsoft Press, 2002 and [Best Practices for the Security APIs](https://msdn.microsoft.com/library/windows/desktop/ms717796).

## Input Validation

The following control messages can present security problems.

-   [**CB\_GETLBTEXT**](cb-getlbtext.md)
-   [**LVM\_GETISEARCHSTRING**](lvm-getisearchstring.md)
-   [**SB\_GETTEXT**](sb-gettext.md)
-   [**SB\_GETTIPTEXT**](sb-gettiptext.md)
-   [**TB\_GETBUTTONTEXT**](tb-getbuttontext.md)
-   [**TTM\_GETTEXT**](ttm-gettext.md)
-   [**TVM\_GETISEARCHSTRING**](tvm-getisearchstring.md)

If the text changes between the call to get the text length and the time the text is displayed or used, a buffer overrun can occur. To avoid this, you must validate the string before using it. In addition, the messages that retrieve text, [**CB\_GETLBTEXT**](cb-getlbtext.md), [**TB\_GETBUTTONTEXT**](tb-getbuttontext.md), and [**TTM\_GETTEXT**](ttm-gettext.md), have no buffer size parameter that presents the potential for a buffer overrun.

When you use [**CB\_GETLBTEXT**](cb-getlbtext.md) or [**SB\_GETTEXT**](sb-gettext.md), you should first call [**CB\_GETLBTEXTLEN**](cb-getlbtextlen.md) or [**SB\_GETTEXTLENGTH**](sb-gettextlength.md) to obtain the buffer size. Some of these messages, [**TB\_GETBUTTONTEXT**](tb-getbuttontext.md), [**LVM\_GETISEARCHSTRING**](lvm-getisearchstring.md), and [**TVM\_GETISEARCHSTRING**](tvm-getisearchstring.md), can be called with a **NULL** parameter value to obtain the length of the string before invoking the message to retrieve the string.

A message that you should pay particular attention to is the status bar [**SB\_GETTIPTEXT**](sb-gettiptext.md) message. This message provides no way to query the length of the string that is to be retrieved.

## Password Use

If you use password-protected edit controls ([**ES\_PASSWORD**](edit-control-styles.md#es-password) style), the buffer that contains the retrieved text must be set to zero as soon as possible to avoid exposing the user's password in memory.

## Security Alerts

The following table lists features that, if used incorrectly, can compromise the security of your applications. The messages listed here do not provide a parameter that specifies the buffer size.



| Feature                                               | Mitigation                                                                                                                                              |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DlgDirListComboBox**](dlgdirlistcombobox.md)      | Make sure the buffer used by the function can be written to and is null-terminated.                                                                     |
| [**CB\_GETLBTEXT**](cb-getlbtext.md)                 | Call [**CB\_GETLBTEXTLEN**](cb-getlbtextlen.md) to obtain the buffer size, and then call [**CB\_GETLBTEXT**](cb-getlbtext.md) to retrieve the string. |
| [**LVM\_GETISEARCHSTRING**](lvm-getisearchstring.md) | Call the message with a **NULL** parameter value to obtain the buffer size, and then call the message a second time to retrieve the string.             |
| [**SB\_GETTEXT**](sb-gettext.md)                     | Call [**SB\_GETTEXTLENGTH**](sb-gettextlength.md) to obtain the buffer size, and then call [**SB\_GETTEXT**](sb-gettext.md) to retrieve the string.   |
| [**TB\_GETBUTTONTEXT**](tb-getbuttontext.md)         | Call the message with a **NULL** parameter value to obtain the buffer size, and then call the message a second time to retrieve the string.             |
| [**TTM\_GETTEXT**](ttm-gettext.md)                   | This message does not provide a way for you to know or specify the size of the buffer.                                                                  |
| [**TVM\_GETISEARCHSTRING**](tvm-getisearchstring.md) | Call the message by passing a **NULL** parameter value to obtain the buffer size, and then call the message a second time to retrieve the string.       |



 

## Related topics

<dl> <dt>

**Other Resources**
</dt> <dt>

[Microsoft Security]( http://go.microsoft.com/fwlink/p/?linkid=193968)
</dt> <dt>

[Security](https://msdn.microsoft.com/library/windows/desktop/ee663293)
</dt> <dt>

[TechNet Security Resources]( http://go.microsoft.com/fwlink/p/?linkid=196444)
</dt> <dt>

[Best Practices for the Security APIs](https://msdn.microsoft.com/library/windows/desktop/ms717796)
</dt> </dl>

 

 




