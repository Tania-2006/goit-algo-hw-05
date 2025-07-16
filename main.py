import sys
from typing import List, Dict


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Парсить рядок логу у словник з ключами:
    'date', 'time', 'level', 'message'
    """
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        # Якщо рядок некоректний — повертаємо пустий словник
        return {}
    date, time, level, message = parts
    return {
        'date': date,
        'time': time,
        'level': level.upper(),
        'message': message
    }


def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Завантажує логи з файлу, повертає список словників.
    Ігнорує некоректні рядки.
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Фільтрує список логів за рівнем логування (case-insensitive).
    """
    level = level.upper()
    return list(filter(lambda log: log['level'] == level, logs))


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Підраховує кількість записів для кожного рівня логування.
    """
    counts = {}
    for log in logs:
        lvl = log['level']
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Виводить таблицю з кількістю записів за рівнем логування.
    """
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print(f"{'-'*17}-|{'-'*8}")
    for level, count in sorted(counts.items()):
        print(f"{level:<17} | {count:<8}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py path/to/logfile.log [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
