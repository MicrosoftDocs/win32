---
description: "Learn more about: JET_SNT"
title: JET_SNT
TOCTitle: JET_SNT
ms:assetid: 74ac5142-8102-4dd3-8f2a-786a7a2ac78f
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269294(v=EXCHG.10)
ms:contentKeyID: 32765586
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_SNT


_**Applies to:** Windows | Windows Server_

## JET_SNT

The [JET_SNT]() group of constants describe the points of the progress of an operation about which information is requested in a call to the [JET_PFNSTATUS](./jet-pfnstatus-callback-function.md) callback function.


| <p>Constant/value</p> | <p>Description</p> | 
|-----------------------|--------------------|
| <p>JET_sntBegin<br />5</p> | <p>The beginning of an operation</p> | 
| <p>JET_sntRequirements<br />7</p> | <p>Not supported.</p><p><strong>Windows 2000 Server:</strong>  The operation is started. In this case, the last parameter of the callback function should be a valid pointer to a <a href="gg269328(v=exchg.10).md">JET_SNPROG</a> structure indicating the total number of units to be executed.</p> | 
| <p>JET_sntProgress<br />0</p> | <p>The number of units completed and number of units yet to be done. This information is returned in the members of a <a href="gg269328(v=exchg.10).md">JET_SNPROG</a> structure.</p> | 
| <p>JET_sntComplete<br />6</p> | <p>The completion of an operation.</p> | 
| <p>JET_sntFail<br />3</p> | <p>The failure of an operation.</p> | 
| <p>JET_sntRecoveryStep<br />8</p> | <p>The recovery control of an operation.</p><div class="alert">&gt; [!NOTE]&gt; <P>This value is not applicable to versions of the Windows operating system starting with Windows 8.</P></div> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_PFNSTATUS](./jet-pfnstatus-callback-function.md)  
[JET_SNP](./jet-snp.md)  
[JET_SNPROG](./jet-snprog-structure.md)
