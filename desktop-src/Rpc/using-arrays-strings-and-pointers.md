---
title: Using Arrays, Strings, and Pointers
description: The Doctor program (see \\samples\\rpc\\doctor in the Platform Software Development Kit (SDK)) is a good example of an application that demonstrates the design trade-offs involved with array and string attributes.
ms.assetid: 9aea94a1-ae1f-4bd6-9dd3-146edf0b5fec
ms.topic: article
ms.date: 05/31/2018
---

# Using Arrays, Strings, and Pointers

The Doctor program (see \\samples\\rpc\\doctor in the Platform Software Development Kit (SDK)) is a good example of an application that demonstrates the design trade-offs involved with array and string attributes. The Doctor program is a small sample version of a better-known program, Eliza, developed by artificial intelligence researcher Joseph Weizenbaum at MIT in the 1960s. The program mimics a therapist by using simple pattern-matching to respond to natural language input.

The Eliza program recorded the following session.



| User                                                | Eliza                                                     |
|-----------------------------------------------------|-----------------------------------------------------------|
| Men are all alike.                                  | In what way?                                              |
| They're always bugging us about something or other. | Can you think of a specific example?                      |
| Well, my boyfriend made me come here.               | Your boyfriend made you come here.                        |
| He says I'm depressed much of the time.             | I am sorry to hear that you are depressed.                |
| It's true, I am unhappy.                            | Do you think coming here will help you not to be unhappy? |
| I need some help; that much seems certain.          | What would it mean to you if you got some help?           |
| Perhaps I could learn to get along with my mother.  | Tell me more about your family.                           |
| My mother takes care of me.                         | Who else in your family takes care of you?                |
| My father.                                          | Your father.                                              |
| You are like my father in some ways.                | What resemblance do you see?                              |



 

The Doctor program can be split into client-side and server-side applications. The client side prompts the patient for input and displays the doctor's response. The server side processes the patient input and generates the doctor's response. This is a classic example of a client-server application: the client is responsible for user interaction while the server handles the extensive computational load. Not much data is passed to and returned by the function but, because the data can require a significant amount of processing, the server processes it.

The Doctor program uses a character array for input and returns another character array as output. The table below lists four ways to pass character arrays between the client and server, and the attributes and functions needed to implement each approach.



| Approach                       | Attributes or functions                                                                                                        |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Counted character arrays       | \[ [size\_is](/windows/desktop/Midl/size-is)\], \[ [length\_is](/windows/desktop/Midl/length-is)\], \[ [ref](/windows/desktop/Midl/ref)\]                                         |
| Stub-managed strings           | \[ [string](/windows/desktop/Midl/string)\], \[ [ref](/windows/desktop/Midl/ref)\], [midl\_user\_allocate](/windows/desktop/Midl/midl-user-allocate-1) on server                  |
| Stub-managed strings           | \[ [string](/windows/desktop/Midl/string)\], \[ [unique](/windows/desktop/Midl/unique)\], [midl\_user\_allocate](/windows/desktop/Midl/midl-user-allocate-1) on client and server |
| Function that returns a string | \[ [unique](/windows/desktop/Midl/unique)\]                                                                                                     |



 

Within the constraints associated with these combinations of attributes, there are alternative ways of sending one character array from client to server and of returning another character array from server to client.

The following topics demonstrate the design trade-offs between the various interfaces that can manage these parameters.

-   [Counted Character Arrays](counted-character-arrays.md)
-   [Strings](strings.md)
-   [Multiple Levels of Pointers](multiple-levels-of-pointers.md)

 

 