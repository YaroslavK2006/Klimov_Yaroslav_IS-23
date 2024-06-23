import sqlite3

# �������� ���������� � ����� ������
conn = sqlite3.connect('�������.db')
cursor = conn.cursor()

# �������� ������� "�������"
cursor.execute('''
CREATE TABLE IF NOT EXISTS ������� (
    id INTEGER PRIMARY KEY,
    �����_������� INTEGER,
    �������_���������� TEXT,
    �����_������������ TEXT,
    �����_������ REAL,
    �����_������ REAL,
    ���_�������� TEXT,
    �����_�������� REAL
)
''')


# ������� ��� ���������� ����� ������ � �������
def ��������_������():
    �����_������� = int(input("������� ����� �������: "))
    �������_���������� = input("������� ������� ����������: ")
    �����_������������ = input("������� ����� ������������: ")
    �����_������ = float(input("������� ����� ������: "))
    �����_������ = float(input("������� ����� ������: "))
    ���_�������� = input("������� ��� ��������: ")
    �����_�������� = float(input("������� ����� ��������: "))

    cursor.execute('''
        INSERT INTO ������� (�����_�������, �������_����������, �����_������������, �����_������, �����_������, ���_��������, �����_��������)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
    �����_�������, �������_����������, �����_������������, �����_������, �����_������, ���_��������, �����_��������))
    conn.commit()


# ������� ��� ������ ������ � �������
def �����_������():
    �����_������� = int(input("������� ����� ������� ��� ������: "))
    cursor.execute('''
        SELECT * FROM �������
        WHERE �����_������� = ?
    ''', (�����_�������,))
    result = cursor.fetchone()
    if result:
        print("��������� ������:")
        print(f"� �������: {result[1]}")
        print(f"�������: {result[2]}")
        print(f"����� ������������: {result[3]}")
        print(f"������: {result[4]}")
        print(f"�����: {result[5]}")
        print(f"��� ��������: {result[6]}")
        print(f"����� ��������: {result[7]}")
    else:
        print("������ �� �������.")


# ������� ��� �������� ������ �� �������
def �������_������():
    �����_������� = int(input("������� ����� ������� ��� ��������: "))
    cursor.execute('''
        DELETE FROM �������
        WHERE �����_������� = ?
    ''', (�����_�������,))
    conn.commit()
    print("������ ������� �������.")


# ������� ��� �������������� ������ � �������
def �������������_������():
    �����_������� = int(input("������� ����� ������� ��� ��������������: "))
    cursor.execute('''
        SELECT * FROM �������
        WHERE �����_������� = ?
    ''', (�����_�������,))
    result = cursor.fetchone()
    if result:
        print("��������� ������:")
        print(f"� �������: {result[1]}")
        print(f"�������: {result[2]}")
        print(f"����� ������������: {result[3]}")
        print(f"������: {result[4]}")
        print(f"�����: {result[5]}")
        print(f"��� ��������: {result[6]}")
        print(f"����� ��������: {result[7]}")

        �����_�����_������� = int(input("������� ����� ����� ������� (�������� ������, ���� �� ����������): "))
        if �����_�����_�������:
            cursor.execute('''
                UPDATE �������
                SET �����_������� = ?
                WHERE �����_������� = ?
            ''', (�����_�����_�������, �����_�������))
        �����_�������_���������� = input("������� ����� ������� ���������� (�������� ������, ���� �� ����������): ")
        if �����_�������_����������:
            cursor.execute('''
                UPDATE �������
                SET �������_���������� = ?
                WHERE �����_������� = ?
            ''', (�����_�������_����������, �����_�������))
        �����_�����_������������ = input("������� ����� ����� ������������ (�������� ������, ���� �� ����������): ")
        if �����_�����_������������:
            cursor.execute('''
                UPDATE �������
                SET �����_������������ = ?
                WHERE �����_������� = ?
            ''', (�����_�����_������������, �����_�������))
        �����_�����_������ = float(input("������� ����� ����� ������ (�������� ������, ���� �� ����������): "))
        if �����_�����_������:
            cursor.execute('''
                UPDATE �������
                SET �����_������ = ?
                WHERE �����_������� = ?
            ''', (�����_�����_������, �����_�������))
        �����_�����_������ = float(input("������� ����� ����� ������ (�������� ������, ���� �� ����������): "))
        if �����_�����_������:
            cursor.execute('''
                UPDATE �������
                SET �����_������ = ?
                WHERE �����_������� = ?
            ''', (�����_�����_������, �����_�������))
        �����_���_�������� = input("������� ����� ��� �������� (�������� ������, ���� �� ����������): ")
        if �����_���_��������:
            cursor.execute('''
                UPDATE �������
                SET ���_�������� = ?
                WHERE �����_������� = ?
            ''', (�����_���_��������, �����_�������))
        �����_�����_�������� = float(input("������� ����� ����� �������� (�������� ������, ���� �� ����������): "))
        if �����_�����_��������:
            cursor.execute('''
                UPDATE �������
                SET �����_�������� = ?
                WHERE �����_������� = ?
            ''', (�����_�����_��������, �����_�������))
        conn.commit()
        print("������ ������� ���������������.")
    else:
        print("������ �� �������.")


# ������� ���� ���������
while True:
    print("\n1. �������� ������")
    print("2. ����� ������")
    print("3. ������� ������")
    print("4. ������������� ������")
    print("5. ����� �� ���������")
    choice = int(input("�������� ��������: "))

    if choice == 1:
        ��������_������()
    elif choice == 2:
        �����_������()
    elif choice == 3:
        �������_������()
    elif choice == 4:
        �������������_������()
    elif choice == 5:
        break
    else:
        print("�������� �����. ����������, �������� ���� �� ��������� ��������.")

# �������� ���������� � ����� ������
conn.close()