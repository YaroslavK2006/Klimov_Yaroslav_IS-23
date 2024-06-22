# �� ������������� ���������� ����� (text18-11.txt) ������� �� ����� ��� ����������,
# ���������� ������ ����������. ������������ ����� ����, � ������� ��������� ������ ���������� �����.


with open('text18-11.txt', 'r', encoding='utf-8') as file:# C����� ��������� ���� � ������ 'text18-11.txt' � ������ ������ � ���������� 'utf-8'
    content = file.read() # ��� ������ ������ ���������� ����� � ��������� ��� � ���������� content
    punctuation_count = sum([1 for symbol in content if symbol in '.,:;!?'])

print(content)
print('���������� ������ ����������:', punctuation_count)

lines = content.split('\n') # ��� ������ ��������� ���������� ����� �� ������ ����� ��������� ������ ����� ������ � �������� �����������

shortest_line = min(lines, key=len) # ��� ������ ������� ����� �������� ������ � ������ �����.

with open('shortest_line.txt', 'w', encoding='utf-8') as file:
    file.write(shortest_line)