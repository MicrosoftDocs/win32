---
description: The taxonomy described below first distinguishes the control plane that concerns itself with the way a multipoint session is established, from the data plane that deals with the transfer of data among session participants.
ms.assetid: d138347a-826a-4615-afbd-ffa7726a47eb
title: Multipoint Taxonomy and Glossary
ms.topic: article
ms.date: 05/31/2018
---

# Multipoint Taxonomy and Glossary

The taxonomy described below first distinguishes the control plane that concerns itself with the way a multipoint session is established, from the data plane that deals with the transfer of data among session participants.

In the control plane, there are two distinct types of session establishment:

-   rooted
-   nonrooted

For a rooted control plane, there exists a special participant, called c\_root, that is different from the rest of the members of this multipoint session, each of which is called a c\_leaf. The c\_root must remain present for the whole duration of the multipoint session, as the session will be broken up in the absence of the c\_root. The c\_root usually initiates the multipoint session by setting up the connection to a c\_leaf, or a number of c\_leafs. The c\_root may add more c\_leafs, or (in some cases) a c\_leaf can join the c\_root at a later time. Examples of the rooted control plane can be found in ATM and ST-II.

For a nonrooted control plane, all members belonging to a multipoint session are leaves, that is, no special participant acting as a c\_root exists. Each c\_leaf needs to add itself to a pre-existing multipoint session that either is always available (as in the case of an IP multicast address), or has been set up through some OOB mechanism which is outside the scope of this discussion (and hence not addressed in the proposed Windows Sockets extensions). Another way to look at this is that a c\_root still exists, but can be considered to be in the network cloud as opposed to one of the participants. Because a control root still exists, a nonrooted control plane could also be considered to be implicitly rooted. Examples of this kind of implicitly rooted multipoint schemes are: a teleconferencing bridge, the IP multicast system, a Multipoint Control Unit (MCU) in an H.320 video conference, etc.

In the data plane, there are also two types of data transfer styles:

-   rooted
-   nonrooted

In a rooted data plane, a special participant called d\_root exists. Data transfer only occurs between the d\_root and the rest of the members of this multipoint session, each of which is referred to as a d\_leaf. The traffic could be unidirectional, or bidirectional. The data sent out from the d\_root will be duplicated (if required) and delivered to every d\_leaf, while the data from d\_leafs will only go to the d\_root. In the case of a rooted data plane, there is no traffic allowed among d\_leafs. An example of a protocol that is uses a rooted data plane is ST-II.

In a nonrooted data plane, all the participants are equal in the sense that any data they send will be delivered to all the other participants in the same multipoint session. Likewise each d\_leaf node will be able to receive data from all other d\_leafs, and in some cases, from other nodes which are not participating in the multipoint session as well. No special d\_root node exists. IP-multicast is an example of a protocol that uses a nonrooted data plane.

Note that the question of where data unit duplication occurs, or whether a shared single tree or multiple shortest-path trees are used for multipoint distribution are protocol issues. As such, they are irrelevant to the interface the client would use to perform multipoint communications. Therefore these issues are not addressed by the Windows Sockets interface.

The following table depicts the taxonomy described above and indicates how existing schemes fit into each of the control and data plane categories. Note that there does not appear to be any multipoint schemes that employ a nonrooted control plane along with a rooted data plane.

| Data plane           | Rooted control plane examples | Nonrooted (implicit rooted) control plane examples |
|----------------------|-------------------------------|----------------------------------------------------|
| Rooted data plane    | ATM, ST-II                    | No known examples                                  |
| Nonrooted data plane | T.120                         | IP-multicast, H.320 (MCU)                          |



 

 

 



