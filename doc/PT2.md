# <div align='center'> Project Stage 2 </div>

## <div align='center'>Group 103<div align='center'>
### <div align='center'>Zijian Pei, Zhangyu Feng, Zhexuan Yin, Jixuan Lu<div align='center'>



# ER Diagram:



![](C:\users\jixua\OneDrive\Desktop\Untitled Diagram.drawio.png))

<div style="page-break-after: always;"></div>

# Assumption and Entity Description:



## Product: 

​	Product is on the top of the hierarchy structure to its subclasses, including CPU, Motherboard, GPU, and Memory. Product is uniquely identified by ProductID. It also contains Name, Price and BrandName as additional attributes. ProductID, which is referenced by different accessory tables, is the primary key of CPU, GPU, MotherBoard and Memory as well.



## CPU: 

​	CPU is a sub-entity of Product and is uniquely identified by ProductID, which is the primary key. ProductID is also a foreign key that references to Product table. CPU has two additional attributes, socket and TDP. Socket is the socket type of the CPU and TDP is the thermal design power that the CPU can take.



## Motherboard: 

​	Motherboard is a sub-entity of Product and is uniquely identified by ProductID, which is the primary key. ProductID is also a foreign key that references to Product table. Motherboard has three additional attributes: socket, supportMemoryType, and ChipSet. Socket is the socket type for the MotherBoard which is used to adapt with CPU. SupportMemoryType is the Memory socket type which is used to adapt with Memory. ChipSet is an important parameter of the modern motherboeard.



## Memory: 

​	Memory is a sub-entity of Product and is uniquely identified by ProductID, which is the primary key. ProductID is also a foreign key that references to Product table. Memory has two additional attributes, Type and Size. Size determines the memory capacity of the memory chip and Type determines what type of memory it is, such as DDR4 and DDR3 RAM. Type is used to adapt with MotherBoard. 



## GPU: 

​	GPU is a sub-entity of Product and is uniquely identified by ProductID, which is the primary key. ProductID is also the foreign key that references to Product table. GPU has three additional attributes, Model, MemorySize, and TDP. Model attribute determines the model of current GPU, MemorySize determines the memory size of the current GPU and TDP is the thermal design power that the GPU can take.

<div style="page-break-after: always;"></div>

## User: 

​	User is a strong entity set that contains user information, it has five attributes: AccountNumber, password, Name, PhoneNumber, and UserType. AccountNumber is the primary key;  User is uniquely identified by AccountNumber, which is used when logging in to our system. Password is the password for the specific user account. With correct match of a AccountNumber and the password, a user can log in to our system. Name and PhoenNumber are additional parts of the profile of the user. UserType defines whether the user is an administrator or just a client of our platform, as different types of users will have different permissions on our database system. 



## CustomizePC: 

​	CustomizePC is a weak entity that needs to be identified by both the PCID and AccountNumber of a user. For each CustomizePC it can have at most one CPU, one GPU, one Memory, and one Motherboard. This information is stored as CPUID, GPUID, RAMID, and MBID in the table, and all of that are foreign keys that reference to ProductID in their own tables. For example, CPUID reference to the ProductID in CPU table. 





# Relation Description:



## ISA Relation: 

A product can be either a CPU, a motherboard, a memory, or a GPU, therefore we use the “ISA” relationship to indicate this relation. Each component of CPU, GPU, MotherBoard and Memory should have a ProductID as the primary key to determine its uniqueness. ProductId is stored as a foreign key and a primary key in the tables of CPU, GPU, MotherBoard, and Memory.



## CPU and MotherBoard Compatibility Relation:

For CPU and Motherboard, we need to check if the socket of the CPU is the same as that of a MotherBoard. If they two have the same socket, then they are compatible. One CPU can have multiple compatible motherboards, and one motherboard can have multiple compatible CPUs as well. Therefore, this is a many-to-many relationship.



## MotherBoard and Memory Compatibility Relation:

For MotherBoard and Memory, we need to check if the support memory type is the same as the memory type. If the memory type supported by a motherboard matches the memory type of the memory card, then they are compatible. One mother can have multiple compatible memory cards, and one memory card can have multiple compatible motherboards as well. Therefore, this is a many-to-many relationship.



## User Create CustomizePC Relation:

For User and CustomizePC, a user can create customized PCs with his/her choice of CPU, motherboard, memory and GPU. Each component can be picked only once for each computer built by the user. A user is allowed to create multiple computers and each computer created belongs to exactly one user. Therefore, this is a one-to-many relationship.



## CPU and CustomizePC Relation:

For CPU and CustomizePC, a CustomizePC can have at most one CPU added, it can also be NULL if the user does not include a CPU in its customized PC. Meanwhile, a CPU can be attached to multiple customized computers built by the users. Therefore, this is a one-to-many relationship.



## MotherBoard and CustomizePC Relation:

For MotherBoard and CustomizePC, a CustomizePC can have at most one MotherBoard added, it can also be NULL if the user does not include a MotherBoard in its customized PC. Meanwhile, a motherboard can be attached to multiple customized computers built by the users. Therefore, this is a one-to-many relationship.



## Memory and CustomizePC Relation:

For Memory and CustomizePC, a CustomizePC can have at most one Memory added, it can also be NULL if the user does not include a Memory in its customized PC. Meanwhile, a memory chip can be attached to multiple customized computers built by the users. Therefore, this is a one-to-many relationship.



## GPU and CustomizePC Relation:

For GPU and CustomizePC, a CustomizePC can have at most one GPU added, it can also be NULL if the user does not include a GPU in its customized PC. Meanwhile, a GPU can be attached to multiple customized computers built by the users. Therefore, this is a one-to-many relationship.

<div style="page-break-after: always;"></div>

# Relational Schema:



~~~sql
Product(ProductID:INT [PK], Price:Real, BrandName:VARCHAR(20), Name:VARCHAR(50))


MotherBoard(ProductID:INT [PK][FK to Product.ProductID], ChipSet:VARCHAR(20), SupportMemoryType:VARCHAR(20), Socket:VARCHAR(20))


Memory(ProductID:INT [PK][FK to Product.ProductID], Size:VARCHAR(20), Type:VARCHAR(20))


GPU(ProductID:INT [PK][FK to Product.ProductID], MemorySize:Int,TDP:INT, Model:VARCHAR(20))


CPU(ProductID:INT [PK][FK to Product.ProductID], TPD:INT,Socket:VARCHAR(20))


User(AccountNumber: INT [PK], Name:VARCHAR(20), password:VARCHAR(20), PhoneNumber:VARCHAR(20), UserType:VARCHAR(20))


CustomizePC(PCID:INT[PK], OwnerNumber:INT [PK][FK to User.AccountNumber], CPUID:INT[FK to CPU.ProductID], MBID:INT[FK to MotherBoard.ProductID], GPUID:INT[FK to GPU.ProductID], RAMID:INT[FK to Memory.ProductID])
~~~

