---
title: WM_DDE_EXECUTE message (Dde.h)
description: A Dynamic Data Exchange (DDE) client application posts a WM\_DDE\_EXECUTE message to a DDE server application to send a string to the server to be processed as a series of commands.
ms.assetid: 23c18a57-83ee-4fd3-a5bc-71645bda34eb
keywords:
- WM_DDE_EXECUTE message Data Exchange
topic_type:
- apiref
api_name:
- WM_DDE_EXECUTE
api_location:
- Dde.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DDE\_EXECUTE message

A Dynamic Data Exchange (DDE) client application posts a **WM\_DDE\_EXECUTE** message to a DDE server application to send a string to the server to be processed as a series of commands. The server application is expected to post a [**WM\_DDE\_ACK**](wm-dde-ack.md) message in response.

To post this message, call the [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) function with the following parameters.


```C++
#define WM_DDE_EXECUTE     0x03E8
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the client window posting the message.

</dd> <dt>

*lParam* 
</dt> <dd>

Contains a global memory object that references an ANSI or Unicode command string, depending on the types of windows involved in the conversation.

</dd> </dl>

## Remarks

The command string is a null-terminated string consisting of one or more opcode strings enclosed in single brackets (\[ \]). Each opcode string has the following syntax, where the *parameters* list is optional:

*opcode parameters*

The *opcode* is any application-defined single token. It cannot include spaces, commas, parentheses, brackets, or quotation marks.

The *parameters* list can contain any application-defined value or values. Multiple parameters are separated by commas, and the entire parameter list is enclosed in parentheses. Parameters cannot include commas or parentheses except inside a quoted string. If a bracket or parenthesis character is to appear in a quoted string, it need not be doubled, as was the case under the old rules.

The following are valid command strings:


```
[connect][download(query1,results.txt)][disconnect] 
[query("sales per employee for each district")] 
[open("sample.xlm")][run("r1c1")] 
[quote_case("This is a "" character")] 
[bracket_or_paren_case("()s or []s should be no problem.")] 
```



Note that, under the old rules, parentheses and brackets had to be doubled, as follows:


```
[bracket_or_paren_case("(())s or [[]]s should be no problem.")] 
```



Servers should be able to parse commands in either form.

Unicode execute strings should be used only when both the client and server window handles cause the [**IsWindowUnicode**](/windows/desktop/api/winuser/nf-winuser-iswindowunicode) function to return **TRUE**.

### Posting

The client application allocates the global memory object by calling the [**GlobalAlloc**](/windows/desktop/api/winbase/nf-winbase-globalalloc) function.

When processing the [**WM\_DDE\_ACK**](wm-dde-ack.md) message that the server posts in reply to a **WM\_DDE\_EXECUTE** message, the client application must delete the object returned by the **WM\_DDE\_ACK** message.

### Receiving

The server application posts the [**WM\_DDE\_ACK**](wm-dde-ack.md) message to respond positively or negatively. The server should reuse the global memory object.

Unless specified otherwise by a sub-protocol, the server should not post the [**WM\_DDE\_ACK**](wm-dde-ack.md) message until all the actions specified by the execute command string are completed. The one exception to this rule is when the string causes the server to terminate the conversation.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>Dde.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**IsWindowUnicode**](/windows/desktop/api/winuser/nf-winuser-iswindowunicode)
</dt> <dt>

[**PackDDElParam**](/windows/desktop/api/Dde/nf-dde-packddelparam)
</dt> <dt>

[**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea)
</dt> <dt>

[**ReuseDDElParam**](/windows/desktop/api/Dde/nf-dde-reuseddelparam)
</dt> <dt>

[**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage)
</dt> <dt>

[**UnpackDDElParam**](/windows/desktop/api/Dde/nf-dde-unpackddelparam)
</dt> <dt>

[**WM\_DDE\_ACK**](wm-dde-ack.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[About Dynamic Data Exchange](about-dynamic-data-exchange.md)
</dt> </dl>

 

