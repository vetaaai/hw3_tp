import csv
import random

groups_db = {
    "BTS": ["RM", "Jin", "Suga", "J-hope", "jimin", "V", "Jung Kook"],
    "BLACKPINK": ["Jennie", "Lisa", "Rose", "Jisoo"],
    "SEVENTEEN": ["S.Coups", "Jeonghan", "Joshua", "Jun", "Hoshi", "Wonwoo", "Woozi", "Dino", "Mingyu", "DK", "Seungkwan", "Vernon"],
    "ATEEZ": ["Hongjoong", "Seonghwa", "Yunho", "San", "Mingi", "Wooyoung", "Jeongho"],
    "Stray Kids": ["Bang Chan", "Lee Know", "Changbin", "Hyunjin", "Han", "Felix", "Seungmin", "I.N."],
    "TWICE": ["Nayeon", "Jeongyeon", "Momo", "Sana", "Jihyo", "Mina", "Dahyun", "Chaeyoung", "Tzuyu"],
    "DAY6": ["Sungjin", "Young K", "Wonpil", "Dowoon"],
    "G-IDLE": ["Minnie", "Miyeon", "Soyeon", "Yuqi", "Shuhua"],
    "aespa": ["Karina", "Giselle", "Winter", "NingNing"],
    "LE SSERAFIM": ["Sakura", "Chaewon", "Huh Yunjin", "Kazuha", "Eunchae"],
    "IVE": ["Gaeul", "Yujin", "Rei", "Wonyoung", "Liz", "Leeseo"],
    "ITZY": ["Yeji", "Lia", "Ryujin", "Chaeryeong", "Yuna"],
    "TXT": ["Soobin", "Yeonjun", "Beomgyu", "Taehyun", "Hueningkai"],
    "ENHYPEN": ["Jay", "Heeseung", "Jake", "Sunghoon", "Sunoo", "Jungwon", "Ni-ki"],
}

labels = ['HYBE', 'SM Entertainment', 'YG Entertainment', 'JYP Entertainment', 'Starship', 'Cube Entertainment', 'KQ Entertainment']
genres = ['K-Pop', 'Hip Hop', 'EDM', 'R&B', 'Ballad', 'Rock']

def generate_csv(filename, num_rows=100):
    groups_list = list(groups_db.keys())
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['group_id', 'group_name', 'label', 'debut_year', 'genre', 'album_sales', 'monthly_listeners'])
        for i in range(1, num_rows + 1):
            group = random.choice(groups_list)
            label = random.choice(labels)
            debut_year = random.randint(2010, 2023)
            genre = random.choice(genres)
            album_sales = round(random.uniform(0.5, 50.0), 1)
            listeners = round(random.uniform(0.1, 25.0), 1)
            writer.writerow([i, group, label, debut_year, genre, album_sales, listeners])

if __name__ == "__main__":
    generate_csv('/data/data.csv', num_rows=100)