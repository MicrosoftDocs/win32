---
title: Fundamental Units
description: Fundamental Units
ms.assetid: 'd450cfa4-59fb-42e0-94a8-7e8bb0559060'
keywords: ["unit of composition", "session", "session groups"]
---

# Fundamental Units

In dealing with profiles, there are two concepts, the declarative high-level language for ETW configurations and the operational ETW runtime objects exposed by the API.

Within this documentation, concepts in the high-level language will be referred to by names such as profile, session, provider, and so forth. The ETW runtime objects are prefixed with ETW, such as ETW session, ETW provider, and so forth.

In general, there are three fundamental units of composition used to build ETW sessions as explained in the following table.



| Unit of Composition                      | Use                                                                                                                 |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Sessions and session groups<br/>   | To configure the aspects of one or more underlying ETW session.<br/>                                          |
| Providers and provider groups<br/> | To configure the aspects of one or more ETW providers.<br/>                                                   |
| Profiles and profile groups<br/>   | To combine one or more sessions and/or session groups with one or more providers and/or provider groups.<br/> |



 

By compiling multiple types of profile configuration to create a configuration for one or more ETW sessions, you actually create a runtime object.

 

 





