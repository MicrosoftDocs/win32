---
title: MIDL Command-Line Reference
description: This section contains reference information for each command-line switch and switch option recognized by the Microsoft RPC MIDL compiler.
ms.assetid: a0e5efb0-a704-4dc5-bd7e-6c98466a2874
keywords:
- Microsoft Interface Definition Language MIDL , reference
- command-line reference MIDL
ms.topic: article
ms.date: 05/31/2018
---

# MIDL Command-Line Reference

This section contains reference information for each command-line switch and switch option recognized by the Microsoft RPC MIDL compiler. Switch entries are arranged in alphabetical order. [General MIDL Command-line Syntax](general-midl-command-line-syntax.md) describes the general command-line syntax.

<dl>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)  
[The Response File Command](the-response-file-command.md)  
[**/acf**](-acf.md)  
[**/align**](-align.md)  
[**/amd64**](-amd64.md)  
[**/app\_config**](-app-config.md)  
[/backward\_compat](-backward-compat.md)  
[**/c\_ext**](-c-ext.md)  
[**/caux**](-caux.md)  
[**/char**](-char.md)  
[**/client**](-client.md)  
[**/confirm**](-confirm.md)  
[**/cpp\_cmd**](-cpp-cmd.md)  
[**/cpp\_opt**](-cpp-opt.md)  
[**/cstruct_out**](-cstruct-out.md)
[**/cstub**](-cstub.md)  
[**/D**](-d.md)  
[**/dlldata**](-dlldata.md)  
[**/env**](-env.md)  
[**/error**](-error.md)  
[**/error**](-error.md)  
[**/h**](-h.md)  
[**/header**](-header.md)  
[**/help (/?)**](-help-.md)  
[**/ia64**](-ia64.md)  
[**/I**](-i.md)  
[**/iid**](-iid.md)  
[**/import**](-import.md)  
[**/lcid**](-lcid.md)  
[**/mktyplib203**](-mktyplib203.md)  
[**/ms\_ext**](-ms-ext.md)  
[**/ms\_union**](-ms-union.md)  
[**/msc\_ver**](-msc-ver.md)  
[**/new**](-new.md)  
[**/newtlb**](-newtlb.md)  
[**/no\_cpp, /nocpp**](-no-cpp-nocpp.md)  
[**/no\_default\_epv**](-no-default-epv.md)  
[**/no\_def\_idir**](-no-def-idir.md)  
[**/no\_format\_opt**](-no-format-opt.md)  
[**/no\_robust**](-no-robust.md)  
[**/no\_warn**](-no-warn.md)  
[**/nologo**](-nologo.md)  
[**/notlb**](-notlb.md)  
[**/o**](-o.md)  
[**/Oi**](-oi.md)  
[**/old**](-old.md)  
[**/oldtlb**](-oldtlb.md)  
[**/oldnames**](-oldnames.md)  
[**/Os**](-os.md)  
[**/osf**](-osf.md)  
[**/out**](-out.md)  
[**/pack**](-pack.md)  
[**/prefix**](-prefix.md)  
[**/protocol**](-protocol.md)  
[**/proxy**](-proxy.md)  
[**/robust**](-robust.md)  
[**/rpcss**](-rpcss.md)  
[**/sal**](-sal.md)  
[**/sal\_local**](-sal-local.md)  
[**/saux**](-saux.md)  
[**/savePP**](-savepp.md)  
[**/sstub**](-sstub.md)  
[**/syntax\_check**](-syntax-check.md)  
[**/<system>**](-system-.md)  
[**/target**](-target.md)  
[**/tlb**](-tlb.md)  
[**/U**](-u.md)  
[**/use\_epv**](-use-epv.md)  
[**/version\_stamp**](-version-stamp.md)  
[**/W**](-w.md)  
[**/warn**](-warn.md)  
[**/win32**](-win32.md)  
[**/win64**](-win64.md)  
[**/WX**](-wx.md)  
[**/Zp**](-zp.md)  
[**/Zs**](-zs.md)  
</dl>

The MIDL compiler can generate code for different platforms and system releases. Consult the [**/target**](-target.md) switch to learn more about suggested switches and how to generate code optimized for a given release.

Note that the minus sign (–) may be substituted for the slash (/) in all MIDL command-line switches that begin with a slash (/). The following example demonstrates their equivalence when invoking the MIDL compiler.

## Examples

**midl /acf my\_acf.acf** *filename***.idl**

**midl -acf my\_acf.acf** *filename***.idl**

 

 




