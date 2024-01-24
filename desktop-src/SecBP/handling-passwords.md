---
description: Currently, user name and password credentials are the most common credentials used for authentication.
ms.assetid: 1d810f71-9bf5-4c5c-a573-c35081f604cf
title: Handling Passwords
ms.topic: article
ms.date: 05/31/2018
---

# Handling Passwords

Currently, user name and password credentials are the most common credentials used for authentication. Even though other types of credentials, such as certificates and biometrics, are starting to find their way into the world of systems and networking, they are often backed up by passwords. And, even where certificates are used, their encryption keys must be protected. So, user names and passwords will continue to be used for credentials well into the foreseeable future.

Given that passwords and encryption keys are going to be around a while, it is important that software systems use them in a secure fashion. If a network or computer system is to remain secure, passwords must be protected from would-be intruders. This might, at first, seem trivial. However, system after system and network after network have been compromised because an attacker has been able to sniff out users' passwords. The problems range from users sharing their passwords with someone, to software that can be penetrated by an attacker.

It is impossible to store secret information in software in a completely secure fashion. And because storing passwords and encryption keys in a software system can never be completely secure, it is recommended that they not be stored in a software system.

However, when passwords must be stored in a software system, which is usually the case, there are precautions that can be taken. The primary precaution is to make it as difficult as possible for an intruder to discover a password. Just like locking your house doors, if someone is determined to break in, it is nearly impossible to prevent them from doing so. But hopefully, you will have raised the level of difficulty sufficiently that the would-be intruder would rather find easier prey.

There are many ways to make an attacker's job of discovering passwords harder. However, the extent of what can actually be done is usually a trade-off with what the users of the network or system are willing to live with. For example, take the case where "single sign on" is not used, and the user is prompted for a password every time an application is started. In most cases, this would create a significant burden on the users, and they would probably complain. Not only that, but lack of a single sign on is inefficient and would degrade the productivity of the users. So, practically speaking, a password generally is not collected from a user except at the time of log on.

Given that passwords must usually be stored on the software system, it becomes important to ensure that passwords are kept as secure as possible and that convenience for users is maintained. For more information, see the following topics:

-   [Password Threat Assessment](password-threat-assessment.md)
-   [Threat Mitigation Techniques](threat-mitigation-techniques.md)

> [!Note]  
> When you have finished using passwords in applications, clear the sensitive information from memory by calling the [**SecureZeroMemory**](/previous-versions/windows/desktop/legacy/aa366877(v=vs.85)) function.

 

 

 
