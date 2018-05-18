---
title: Providing MUI-Compliant Help Files
description: MMC 2.0 supports Multilingual User Interface systems by allowing a snap-in to use online Help files created for the user's specific language.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '01a13430-e64e-4e3a-8db9-1d42ad9b32bb'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Providing MUI-Compliant Help Files

MMC 2.0 supports [Multilingual User Interface](_win32_multilingual_user_interface) systems by allowing a snap-in to use online Help files created for the user's specific language. If the user's language is not U.S. English, then MMC 2.0 searches for the online Help file based on the following location.


```C++
<dir>\mui\<langid>\<helpfile>
```



<dl> <dt>

<span id="dir"></span><span id="DIR"></span>dir
</dt> <dd>

If helpfile contains a fully qualified path, then dir is the supplied path. If helpfile does not contain a fully qualified path, then dir is %SystemRoot%\\Help.

</dd> <dt>

<span id="langid"></span><span id="LANGID"></span>langid
</dt> <dd>

The 4-digit hexadecimal [language identifier](https://msdn.microsoft.com/library/windows/desktop/dd318693) of the user's user interface language.

</dd> <dt>

<span id="helpfile"></span><span id="HELPFILE"></span>*helpfile*
</dt> <dd>

The name of the online Help file, as provided by the snap-in when MMC calls the [**ISnapinHelp2::GetHelpTopic**](isnapinhelp2-gethelptopic.md) method.

> [!Note]  
> For MUI to be in effect, the user's user interface language can be other than U.S. English, but the system's user interface language must be U.S. English. It is the snap-in provider's responsibility to provide the online Help file in the user's user interface language.

 

</dd> </dl>

## Related topics

<dl> <dt>

[Registering Snap-in Names](registering-snap-in-names.md)
</dt> </dl>

 

 




