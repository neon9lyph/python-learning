# 老土写法 (3行)
res = []
for x in [1, 2, 3]:
    res.append(x * 10)

# 性感写法 (1行)
res = [x * 10 for x in [1, 2, 3]]
# 结果: [10, 20, 30]

print(res)


users = ["Admin", "Guest", "SuperAdmin", "Bot_01"]
# 只要真人和管理员，踢掉机器人
real_humans = [f"{u} (Latest)" for u in users if "Bot" not in u and len(u) > 5]
# 等同于js
# const real_humans = []
# for (const u of users) {
#     if (!u.includes("Bot") && u.length > 5) {
#         real_humans.push(`${u} (Latest)`);
#     }
# }

# 结果: ['SuperAdmin (Latest)']
print(real_humans)


scores = [100, -1, 85]
# 把 -1 变成 0
clean_scores = [f"{s:.2f}" if s > 0 else f"不及格:{-s:.2f}" for s in scores]
# 等同于js
# for (const s of scores) {
#     if (s > 0) {
#         clean_scores.push(s.toFixed(2));
#     } else {
#         clean_scores.push(`不及格:${(-s).toFixed(2)}`);
#     }
# }
# 结果: [100.00, "不及格:1.00", 85.00]
print(clean_scores)


num_info = [[1, 2], [3, 4], [5, 6, 7], [8, [9, 10]]]
flattened = [n for sublist in num_info for n in sublist if isinstance(n, int)]
# 等同于js
# const flattened = [];
# for (const sublist of num_info) {
#     for (const n of sublist) {
#         if (typeof n === "number") {
#             flattened.push(n);
#         }
#     }
# }
print(flattened)  # 结果: [1, 2, 3, 4, 5, 6]
