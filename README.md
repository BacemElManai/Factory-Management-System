# Factory-Management-System
🏭 Factory Management System
A sophisticated Python-based Factory Management System designed for efficient handling of manufacturing facility records with robust data validation, secure storage, and intelligent reporting capabilities.

🚀 Features
🔐 Advanced Data Validation
Factory Name: Uppercase only, max 10 characters with real-time validation

Employee Count: Minimum threshold enforcement (>10 employees)

Revenue Tracking: Non-negative revenue validation

Factory ID System: Exactly 8-digit unique identifier with numeric validation

Director Information: Alphabetic only, max 20 characters

💾 Smart Data Management
Binary Storage: Secure pickle-based serialization for factories.dat

Automatic Sorting: Descending order by employee count using insertion sort algorithm

Geographic Filtering: Specialized export for Tunis-based facilities

Memory Efficiency: NumPy array optimization for record handling

📊 Professional Reporting
Complete Record Display: Formatted output of all factory data

Regional Analytics: Dedicated Tunis facility reporting to factories_tunis.txt

User-Friendly Interface: Intuitive menu system with error handling

🛠 Technical Architecture
Data Model

factory = dict(
    name=str,           # Uppercase, max 10 chars
    employees=int,      # Minimum 11
    revenue=float,      # Non-negative
    address=str,        # Free text
    id=str,             # Exactly 8 digits
    director=str        # Alphabetic, max 20 chars
)
Core Modules
Validation Engine: Custom is_alpha() and is_upper() functions

Data Persistence: Binary serialization/deserialization with error handling

Sorting Algorithm: Optimized insertion sort for employee-based ranking

Menu Controller: Continuous operation with graceful exit handling

📋 Usage

python factory_management.py
Menu Options
Add Factory: Complete data entry with guided validation

Show All Factories: Display all records in employee-descending order

Show Tunis Factories: Export and display facilities in Tunis region

🎯 Business Value
Operational Efficiency: Streamlined factory data management

Data Integrity: Comprehensive validation ensures database quality

Decision Support: Sorted reporting enables strategic workforce analysis

Regional Planning: Specialized geographic filtering for location-based strategies

🔧 Technical Excellence
Modular Design: Separated validation, core functions, and UI layers

Memory Management: NumPy array optimization for record storage

Error Resilience: Robust exception handling for file operations

Code Quality: Type hints, structured loops, and professional formatting

📁 Output Files
factories.dat: Secure binary database of all factory records

factories_tunis.txt: Formatted text report of Tunis-based facilities

📊 Sample Output

=== 🏭 Factory Management Menu ===
1 - Add Factory
2 - Show All Factories
3 - Show Factories in Tunis

Factory name (≤ 10 chars, uppercase only): MANUFACTURE
Employees: 150
Revenue: 5000000
Address: Tunis
Factory ID: 12345678
Director: John Smith

✅ Tunis factories exported to factories_tunis.txt
🚦 Validation Examples
✅ "FACTORY" - Valid (uppercase, ≤10 chars)

❌ "factory" - Invalid (not uppercase)

❌ "VERYLONGFACTORYNAME" - Invalid (>10 chars)

✅ "12345678" - Valid Factory ID

❌ "1234" - Invalid Factory ID (not 8 digits)

💡 Ideal For
Manufacturing companies managing multiple facilities

Supply chain and operations managers

Business intelligence and data analysis projects

Python developers demonstrating file I/O and validation skills

This system represents production-ready code with professional error handling, data validation, and modular architecture suitable for enterprise environments.
