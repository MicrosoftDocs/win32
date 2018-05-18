---
title: HH\_PRETRANSLATEMESSAGE command
description: This command is called in the message loop of your Windows application to ensure proper handling of Windows messages, especially keyboard messages when running HTML Help single thread.
ms.assetid: '64D497B8-B76B-4472-87CD-01C1A2969685'
---

# HH\_PRETRANSLATEMESSAGE command

This command is called in the message loop of your Windows application to ensure proper handling of Windows messages, especially keyboard messages when running HTML Help single thread.

The HTML Help API is not thread safe and must be called from one and only one thread in a process.



| *pszFile*     | *dwData*                             |
|---------------|--------------------------------------|
| Must be NULL. | Points to a Win32 **MSG** structure. |



 

## Example


```
MSG msg;
while (GetMessage (&amp;msg, NULL, 0, 0))  // Retrieve a message from the
 {                                     // calling thread's message queue
  if (!HtmlHelp (
                 NULL,
                 NULL,
                 HH_PRETRANSLATEMESSAGE,
                 &amp;msg))
    {
     TranslateMessage (&amp;msg);
     DispatchMessage (&amp;msg);
    }
 }
 
```



## Return Value

-   True, if message is translated.
-   False, if command fails.

## Remarks

-   The **MSG** structure contains message information from a thread's message queue.
-   Before calling this command, you must first set the global property **HH\_GPROPID\_SINGLETHREAD** to VARIANT\_TRUE by calling the [HH\_INITIALIZE](hh-initialize-command.md) command.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_INITIALIZE](hh-initialize-command.md)
</dt> <dt>

[HH\_UNINITIALIZE](hh-uninitialize-command.md)
</dt> </dl>

 

 




