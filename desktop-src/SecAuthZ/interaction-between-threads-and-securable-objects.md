---
Description: 'In an access check, the system compares the security information in the thread's access token against the security information in the object's security descriptor.'
ms.assetid: '40871179-d383-43d0-810d-0805c88dbbd6'
title: Interaction Between Threads and Securable Objects
---

# Interaction Between Threads and Securable Objects

When a thread attempts to use a [securable object](securable-objects.md), the system performs an access check before allowing the thread to proceed. In an access check, the system compares the security information in the thread's [*access token*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-token-gly) against the security information in the object's [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly).

-   The access token contains [*security identifiers*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SIDs) that identify the user associated with the thread.
-   The security descriptor identifies the object's owner and contains a [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL). The DACL contains [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs), each of which specify the access rights allowed or denied to a specific user or group.

The system checks the object's DACL, looking for ACEs that apply to the user and group SIDs from the thread's access token. The system checks each ACE until access is either granted or denied or until there are no more ACEs to check. Conceivably, an [*access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL) could have several ACEs that apply to the token's SIDs. And, if this occurs, the access rights granted by each ACE accumulate. For example, if one ACE grants read access to a group and another ACE grants write access to a user who is a member of the group, the user can have both read and write access to the object.

The following illustration shows the relationship between these blocks of security information:

![relationships between processes, aces, and dacls](images/cssec-02.png)

 

 



