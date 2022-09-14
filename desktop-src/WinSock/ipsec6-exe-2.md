---
description: Configuration of IPSec policies and security associations for IPv6 is done with Ipsec6.exe.
ms.assetid: 9a0c8e48-bc57-461d-9ade-54b75f7aa56d
title: Ipsec6.exe
ms.topic: article
ms.date: 05/31/2018
---

# Ipsec6.exe

Configuration of IPSec policies and security associations for IPv6 is done with Ipsec6.exe. The following are Ipsec6.exe subcommands:

<dl> <dt>

<span id="ipsec6_sp__Interface_"></span><span id="ipsec6_sp__interface_"></span><span id="IPSEC6_SP__INTERFACE_"></span>**ipsec6 sp \[***Interface***\]**
</dt> <dd>

Displays active security policies. Alternately, displays active security policies for a specific interface.

</dd> <dt>

<span id="ipsec6_sa"></span><span id="IPSEC6_SA"></span>**ipsec6 sa**
</dt> <dd>

Displays active security associations.

</dd> <dt>

<span id="ipsec6_c__FileName_without_extension__"></span><span id="ipsec6_c__filename_without_extension__"></span><span id="IPSEC6_C__FILENAME_WITHOUT_EXTENSION__"></span>**ipsec6 c \[***FileName(without extension)***\]**
</dt> <dd>

Creates files used to configure security policy and security associations. Creates *FileName*.spd for security policies and *FileName*.sad for security associations. Use the created files as templates to configure security policies or security associations. The files can be modified with a text editor. To invoke the configuration contained in the SPD and SAD files, use the **ipsec6 a** command.

</dd> <dt>

<span id="ipsec6_a__FileName_without_extension__"></span><span id="ipsec6_a__filename_without_extension__"></span><span id="IPSEC6_A__FILENAME_WITHOUT_EXTENSION__"></span>**ipsec6 a \[***FileName(without extension)***\]**
</dt> <dd>

Adds security policies in *FileName*.spd and security associations in *FileName*.sad to the list of active security policies and security associations.

</dd> <dt>

<span id="ipsec6_i__Policy___FileName_without_extension__"></span><span id="ipsec6_i__policy___filename_without_extension__"></span><span id="IPSEC6_I__POLICY___FILENAME_WITHOUT_EXTENSION__"></span>**ipsec6 i \[***Policy***\] \[***FileName(without extension)***\]**
</dt> <dd>

Adds security policies in *FileName*.spd and security associations in *FileName*.sad to the list of active security policies and security associations as referenced by policy number.

</dd> <dt>

<span id="ipsec6_d__type___sp_sa___IndexNumber_"></span><span id="ipsec6_d__type___sp_sa___indexnumber_"></span><span id="IPSEC6_D__TYPE___SP_SA___INDEXNUMBER_"></span>**ipsec6 d \[type = sp sa\] \[***IndexNumber***\]**
</dt> <dd>

Deletes security policies or security associations from the list of active security policies and security associations, as referenced by their index number (displayed with **ipsec6 sp** or **ipsec6 sa**).

</dd> </dl>

 

 



